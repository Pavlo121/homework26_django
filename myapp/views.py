from django.http import HttpResponse

def hello(request):
    return HttpResponse("Django in Docker is working!")
