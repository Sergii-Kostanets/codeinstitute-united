from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import GameForm
from .models import Game
from django.http import JsonResponse
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.db.models import Q

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(status=1).order_by('-created_on')
    template_name = 'connect/game_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if search_query:
            # Filter the queryset based on the search query
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(platform__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        return queryset

    def render_to_response(self, context, **response_kwargs):
        # Check if the request is an AJAX request
        if self.request.is_ajax():
            # Return an empty JSON response for AJAX requests
            return JsonResponse({})
        else:
            # Render the game list template as usual
            return super().render_to_response(context, **response_kwargs)


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'connect/game_create.html'
    success_url = reverse_lazy('game_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Your game connect has been added and is awaiting approval')
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'connect/game_edit.html'
    success_url = reverse_lazy('game_list')

    def form_valid(self, form):
        game = form.save(commit=False)
        game.status = 0
        game.save()
        messages.success(self.request, 'Your game connect has been updated and is awaiting approval')
        return super().form_valid(form)


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'connect/game_delete.html'
    success_url = reverse_lazy('game_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your game connect has been deleted successfully')
        return super().delete(request, *args, **kwargs)


class GamePublishList(ListView):
    model = Game
    template_name = 'connect/game_publish_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')

        if self.request.user.is_staff:
            queryset = queryset.filter(status=0)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(platform__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            game_list_html = render_to_string('connect/game_publish_list_ajax.html', context, request=self.request)
            return JsonResponse({'game_list_html': game_list_html})
        else:
            return super().render_to_response(context, **response_kwargs)


class GamePublish(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'connect/game_publish.html'
    success_url = reverse_lazy('game_list')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        game = form.save(commit=False)
        game.status = 1  # Set the status to 1 (publish)
        game.save()
        messages.success(self.request, 'New game connect has been published successfully.')
        return super().form_valid(form)


class GameConnect(View):
    template_name = 'connect/game_connect.html'
    success_message = 'Thank you for your message!'

    def get(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(status=1)
        game = get_object_or_404(queryset, slug=slug)
        context = {'game': game}
        return render(request, self.template_name, context)


class GamesOfUser(LoginRequiredMixin, generic.ListView):
    template_name = 'connect/game_list_of_user.html'
    context_object_name = 'game_list'
    paginate_by = 5

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        queryset = Game.objects.filter(author=self.request.user).order_by('-created_on')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(platform__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(content__icontains=search_query)
            )

        return queryset
