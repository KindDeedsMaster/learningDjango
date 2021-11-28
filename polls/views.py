from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world. you are at the polls index")


def notindex(request):
    return HttpResponse("you are at polls notindex")


# Create your views here.
