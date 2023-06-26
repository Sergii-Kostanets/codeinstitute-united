from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from .forms import CommentForm

from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


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
                title__icontains=search_query
            ) | queryset.filter(
                excerpt__icontains=search_query
            ) | queryset.filter(
                content__icontains=search_query
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context


class PostDetail(View):
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            post = get_object_or_404(Post, slug=kwargs['slug'], status=1)
        else:
            post = get_object_or_404(Post, slug=kwargs['slug'])

        self.post = post
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        post = self.post

        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been added and is awaiting approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(View):
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
            post.slug = slugify(post.title)
            post.save()
            messages.success(self.request, 'Your post has been created and is awaiting approval')
            return redirect('post_list')
        return render(
            request,
            'blog/post_create.html',
            {
                'form': form,
            },
        )


class PostEdit(View):
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
            messages.success(self.request, 'Your post has been updated and is awaiting approval')
            return redirect('post_list')
        return render(
            request,
            'blog/post_edit.html',
            {
                'form': form,
                'post': post,
            },
        )


class PostDelete(LoginRequiredMixin, View):
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
            messages.error(request, 'You do not have permission to delete this post')

        return redirect('post_list')


class PostPublishList(LoginRequiredMixin, generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'blog/post_publish_list.html'
    paginate_by = 12


class PostPublish(View):
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
            messages.success(self.request, 'The post has been published successfully')
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
        return Post.objects.filter(author=self.request.user).order_by('-created_on')
