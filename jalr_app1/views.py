from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def vistaUno(request):
    html="""
    <h1>Vista 1</h1>
    <h2>Rama 1</h2>
    <h3>Video emocional</h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VN5hrGx866E?si=75NEnpjDyTGp0t2g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    """
    return HttpResponse(html)