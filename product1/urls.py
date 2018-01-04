from django.conf.urls import include, url
from django.contrib import admin
from base.views import shirts
from product1 import settings
import django
from django.views.static import serve

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/home/$', shirts),
    url(r'^pics/(?P<path>.*)$',django.views.static.serve,{'document_root': settings.BASE_DIR+'/pics'}),
]
