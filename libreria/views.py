from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')

def documento(request):
    return render(request, 'paginas/documento.html')

def multimedia(request):
    return render(request, 'paginas/multimedia.html')