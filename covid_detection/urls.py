
from django.contrib import admin
from django.urls import path
from app1.views import home,usignup,ulogin,index,ulogout,contact_us
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('usignup/',usignup, name='usignup'),
    path('ulogin/',ulogin, name='ulogin'),
    path('ulogin/index',index, name='index'),
    path('ulogout/',ulogout, name='ulogout'),
    path('',contact_us, name='contact_us'),


    #  re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

