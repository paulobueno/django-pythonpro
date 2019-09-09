from django.shortcuts import render


def home(request):  # pragma: no cover
    return render(request, 'base/home.html')  # pragma: no cover
