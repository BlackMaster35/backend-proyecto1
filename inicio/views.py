from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("<h1>Buenos días, bienvenidos al servidor </h1>")
