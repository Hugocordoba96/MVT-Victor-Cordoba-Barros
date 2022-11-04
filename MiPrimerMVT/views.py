from django.http import HttpResponse
from django.shortcuts import render

def lista_familiares(request):

    return render(request, 'familiares.html',{'Abuela':'Gloria Reyes', 'EdadAbu':55, 'FechaA':1967, 'Madre':'Claudia Barros', 'EdadM':35,'FechaM':1987, 'Hermana':'Dana Cordoba', 'EdadH':15, 'FechaH':2007})
