from django.shortcuts import render
from base.models import Shirts,Jeans,Jackets,Gymwear,Sunglasses,Watches


def products(request):
    context = {}
    return render(request, 'index.html', context)


def home(request):
    context={}
    return render(request, 'home.html', context)

def shirts(request):
    context={"title":"Shirts"}
    shirts = Shirts.objects.filter(is_active=True)
    context["objs"] = shirts
    return render(request, 'shirts.html', context)

def jeans(request):
    context={"title":"Jeans"}
    jeans = Jeans.objects.filter(is_active=True)
    context["objs"] = jeans
    return render(request, 'shirts.html', context)

def jacket(request):
    context={"title":"Jackets"}
    jackets = Jackets.objects.filter(is_active=True)
    context["objs"] = jackets
    return render(request, 'shirts.html', context)

def gymwear(request):
    context={"title":"Jacket"}
    objs = Gymwear.objects.filter(is_active=True)
    context["objs"] = objs
    return render(request, 'shirts.html', context)

def watches(request):
    context={"title":"Watches"}
    objs = Watches.objects.filter(is_active=True)
    context["objs"] = objs
    return render(request, 'shirts.html', context)

def sunglasses(request):
    context={"title":"Sunglasses"}
    objs = Sunglasses.objects.filter(is_active=True)
    context["objs"] = objs
    return render(request, 'shirts.html', context)
