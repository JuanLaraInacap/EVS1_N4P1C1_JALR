from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def vistaUno(request):
    html="""
    <h1>Matias Fernandez un Crack</h1>
    <h2>Vista 1</h2>
    <h3>Rama 1</h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VN5hrGx866E?si=75NEnpjDyTGp0t2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HttpResponse(html)

def vistaDos(request):
    html="""
    <h1>Colo Colo 2006</h1>
    <h2>Vista 2</h2>
    <h3>Rama 1</h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/3PJro44OOug?si=zRH4976gQCWR4vVj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HttpResponse(html)