from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.core.paginator import Paginator
from django.forms import ValidationError


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        queryset = queryset.filter(status=1)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(author__username__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class PostDetail(View):

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])

        if not request.user.is_staff:
            if post.status == 0 and post.author != request.user:
                raise PermissionDenied

        self.blog_post = post
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        post = self.blog_post

        comments = post.comments.filter(approved=True).order_by('created_on')

        # Paginate the comments
        paginator = Paginator(comments, 30)  # The number of comments per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": page_obj,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = self.blog_post
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment \
            has been added and is awaiting approval')
        else:
            comment_form = CommentForm()
            messages.add_message(request, messages.ERROR, 'Your comment \
            could not be added')

        return redirect(reverse('post_detail', kwargs={'slug': slug}))


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(
            request,
            'blog/post_create.html',
            {
                'form': form,
            },
        )

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.slug:
                post.slug = slugify(post.title)
            try:
                post.full_clean()  # Validate the post model
            except ValidationError as e:
                form.errors['__all__'] = e.messages  # Add the validation error
                return render(
                    request,
                    'blog/post_create.html',
                    {
                        'form': form,
                    },
                )
            post.save()
            messages.success(self.request, 'Your post has been created and is \
            awaiting approval')
            return redirect('post_list')
        return render(
            request,
            'blog/post_create.html',
            {
                'form': form,
            },
        )


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user.is_staff or self.request.user == post.author

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(
            request,
            'blog/post_edit.html',
            {
                'form': form,
                'post': post,
            },
        )

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.status = 0
            post.save()
            messages.success(self.request, 'Your post has been updated and is \
            awaiting approval')
            return redirect('post_list')
        return render(
            request,
            'blog/post_edit.html',
            {
                'form': form,
                'post': post,
            },
        )


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user.is_staff or self.request.user == post.author

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)

        # Check if the post belongs to the current user
        if post.author == request.user:
            post.delete()
            messages.success(request, 'Post deleted successfully')
        elif request.user.is_staff:
            post.delete()
            messages.success(request, 'Post deleted successfully')
        else:
            messages.error(request, 'You do not have permission to delete \
            this post')

        return redirect('post_list')


class PostPublishList(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/post_publish_list.html'
    paginate_by = 12

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return render(request, '403.html', status=403)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if self.request.user.is_staff:
            queryset = queryset.filter(status=0).order_by('-created_on')

            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(excerpt__icontains=search_query) |
                    Q(content__icontains=search_query) |
                    Q(author__username__icontains=search_query)
                )

        else:
            queryset = queryset.none()

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            post_list_html = render_to_string('blog/post_publish_list.html',
                                              context, request=self.request)
            return JsonResponse({'post_list_html': post_list_html})
        else:
            context['post_list'] = context['object_list']
            return super().render_to_response(context, **response_kwargs)


class PostPublish(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return self.request.user.is_staff

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(
            request,
            'blog/post_publish.html',
            {
                'form': form,
                'post': post,
            },
        )

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.status = 1
            post.save()
            messages.success(self.request, 'The post has been published \
            successfully')
            return redirect('post_list')
        return render(
            request,
            'blog/post_publish.html',
            {
                'form': form,
                'post': post,
            },
        )


class PostListUser(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/post_list_user.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if self.request.user.is_authenticated:
            queryset = (
                queryset.filter(author=self.request.user)
                .order_by('-created_on')
            )

            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) |
                    Q(excerpt__icontains=search_query) |
                    Q(content__icontains=search_query)
                )

        else:
            queryset = queryset.none()

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            post_list_html = render_to_string('blog/post_list_user.html',
                                              context, request=self.request)
            return JsonResponse({'post_list_html': post_list_html})
        else:
            context['post_list'] = context['object_list']
            return super().render_to_response(context, **response_kwargs)


class DraftCommentList(UserPassesTestMixin, View):
    template_name = 'blog/draft_comment_list.html'

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        draft_comments = Comment.objects.filter(approved=False)\
            .order_by('created_on')
        return render(request, self.template_name,
                      {'draft_comments': draft_comments})


class ApproveComment(View):
    def get(self, request, comment_id):
        if not request.user.is_staff:
            raise PermissionDenied

        comment = get_object_or_404(Comment, id=comment_id)
        comment.approved = True
        comment.save()

        return redirect('draft_comment_list')


class DeleteComment(View):
    def get(self, request, comment_id):
        if not request.user.is_staff:
            raise PermissionDenied

        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()

        return redirect('draft_comment_list')
