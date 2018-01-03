from django.conf.urls import include, url
from django.contrib import admin
from base.views import shirts
from product1 import settings
import django

urlpatterns = [
    # Examples:
    # url(r'^$', 'product1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/shirts/$', shirts),
    url(r'^pics/(?P<path>.*)$', django.views.static.serve,{'document_root': settings.BASE_DIR+'/static/pics'}),
    # url(r'^pics/(?P<path>.*)$', django.views.static.serve,{'document_root': '/home/ganesh/rikoouu/product1/static/pics'}),
]
# /home/ganesh/rikoouu/product1/static/pics/Firefox_wallpaper.png