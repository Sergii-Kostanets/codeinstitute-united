from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import GameForm
from .models import Game


class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(status=1).order_by('-created_on')
    template_name = 'connect/game_list.html'
    paginate_by = 5


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


class GamePublishList(generic.ListView):
    model = Game
    template_name = 'connect/game_publish_list.html'
    paginate_by = 5

    def get_queryset(self):
        if self.request.user.is_staff:
            return Game.objects.filter(status=0).order_by('-created_on')
        else:
            return Game.objects.none()  # Empty queryset for non-staff users



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
