from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title = "Hello there..."
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    return render(request, "hello_world.html", {"title": title})

def about_page(request):
    return HttpResponse("<h1>About us</h1>")

def contact_page(request):
    return HttpResponse("<h1>Contact us</h1>")