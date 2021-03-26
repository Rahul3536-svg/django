from django.shortcuts import render,HttpResponse
from app2.models import Contact

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")

        contact = Contact(name=name,mobile=mobile,address=address)
        contact.save()
    return render(request, "contact.html")


