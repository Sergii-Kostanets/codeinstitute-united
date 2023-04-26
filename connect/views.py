from django.shortcuts import render


def get_game_list(request):
    return render(request, 'connect/game_list.html')
