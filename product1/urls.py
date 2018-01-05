from django.conf.urls import include, url
from django.contrib import admin
from base.views import products,home,shirts,jeans,jacket,gymwear,watches
from product1 import settings
import django
from django.views.static import serve

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/home/$', products),
    url(r'^api/home/$', home),
    url(r'^api/shirts/$', shirts),
    url(r'^api/jeans/$', jeans),
    url(r'^api/jackets/$', jacket),
    url(r'^api/gymwear/$', gymwear),
    url(r'^api/watches/$', watches),
    url(r'^api/sunglasses/$', watches),
    url(r'^pics/(?P<path>.*)$',django.views.static.serve,{'document_root': settings.BASE_DIR+'/pics'}),
]
