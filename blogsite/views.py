from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'blogsite/index.html', context)