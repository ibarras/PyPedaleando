from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, and Fuck")
    
def detail(request, evento_id):
    return HttpResponse("Buscando el evento %s " % evento_id)