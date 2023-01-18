from django.urls import path
from galeria.views import index, imagem, galeria

urlpatterns = [
    path('', index, name = 'index'),
    path('imagem/<pixelArt_id>', imagem, name='imagem'),
    path('galeria/', galeria, name='galeria')
]

