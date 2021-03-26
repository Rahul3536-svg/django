from django.http import HttpResponse


def run(request):
    return HttpResponse("who are you")