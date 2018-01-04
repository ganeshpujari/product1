from django.shortcuts import render
from base.models import Shirts
def shirts(request):
    try:
        objs=Shirts.objects.all()
        context = {"objs": objs}
        return render(request, 'shirts.html', context)
    except :
        pass