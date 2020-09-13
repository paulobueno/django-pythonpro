from django.urls import path
from base.views import home, triangles

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('triangles', triangles, name='triangles'),
]
