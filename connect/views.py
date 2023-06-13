from django.shortcuts import render, get_object_or_404
from django.views import generic, View

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
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'connect/game_edit.html'
    success_url = reverse_lazy('game_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Game, slug=slug)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        game = self.get_object()
        kwargs['instance'] = game
        return kwargs
