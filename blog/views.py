from django.shortcuts import render


def get_post_list(request):
    return render(request, 'post_list.html')
