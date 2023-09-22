from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaTres(request):
    html="""
    <h1>Mejor Videojuego del Mundo</h1>
    <h2>Vista 3</h2>
    <h3>Rama 2</h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/dqls4wh_zg4?si=K2FV2Q4Jd8sH9XQ-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HttpResponse(html)

def vistaCuatro(request):
    html="""
    <h1>Inacap y sus 7 años acreditado</h1>
    <h2>Vista 4</h2>
    <h3>Rama 2</h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/3mRgumuUIVY?si=RjD6-TmJrKbwHvMI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HttpResponse(html)
