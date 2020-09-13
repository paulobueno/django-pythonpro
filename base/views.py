from django.shortcuts import render


def home(request):  # pragma: no cover
    return render(request, 'base/home.html')  # pragma: no cover


def triangles(request):  # pragma: no cover
    return render(request, 'base/triangles_wall.html')  # pragma: no cover
