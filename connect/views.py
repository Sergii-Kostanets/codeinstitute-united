from django.shortcuts import render, get_object_or_404
from django.views import generic, View


from .models import Game
from .forms import GameForm


class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.filter(status=1).order_by('-created_on')
    template_name = 'connect/game_list.html'
    paginate_by = 5


class GameEdit(View):
    def get(self, request, slug, *args, **kwargs):
        game = Game.objects.get(slug=slug)
        form = GameForm(instance=game)
        return render(request, 'connect/game_edit.html', {'form': form})

    def post(self, request, slug, *args, **kwargs):
        queryset = Game.objects.filter(status=1)
        game = get_object_or_404(queryset, slug=slug)
        
        
        game = Game.objects.get(slug=slug)
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
        return render(request, 'connect/game_edit.html', {'form': form})

