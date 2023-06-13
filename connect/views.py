from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
