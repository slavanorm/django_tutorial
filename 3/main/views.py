from django.http import HttpResponse


def homepage(request):
    return HttpResponse("hello cruel world")
