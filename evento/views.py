from django.shortcuts import render

def index(request):
    template = "index.html"
    welcome_string = "Hello and fuck"
    return render(request, template, locals())
    
def detail(request, evento_id):
    return HttpResponse("Buscando el evento %s " % evento_id)
