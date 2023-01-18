from django.shortcuts import render, get_object_or_404
from galeria.models import PixelArt
# Create your views here.

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request,pixelArt_id):
    pixelArt = get_object_or_404(PixelArt, pk=pixelArt_id)
    return render(request, 'galeria/imagem.html', {"pixelArt":pixelArt})

def galeria(request):
    pixelArts = PixelArt.objects.order_by("name").all()
    return render(request, "galeria/galeria.html", {"cards" : pixelArts})
