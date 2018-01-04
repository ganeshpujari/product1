from django.shortcuts import render
from base.models import Shirts,Jeans,Jackets,Gymwear,Sunglasses,Watches


def products(request):
    context = {}
    try:
        shirts=Shirts.objects.filter(is_active=True)
        context["shirts"]=shirts

        jeans = Jeans.objects.filter(is_active=True)
        context["jeans"]=jeans

        jackets = Jackets.objects.filter(is_active=True)
        context["jackets"]=jackets

        gymwear = Gymwear.objects.filter(is_active=True)
        context["gymwear"]=gymwear

        sunglasses = Sunglasses.objects.filter(is_active=True)
        context["sunglasses"]=sunglasses

        watches = Watches.objects.filter(is_active=True)
        context["watches"]=watches


        return render(request, 'index.html', context)
    except (Exception,)as e :
        print (e)