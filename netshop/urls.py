"""netshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from netshop.settings import DEBUG,MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('goods.urls')),
    path('user/',include('userapp.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    url(r'media/(?P<path>.*)$',serve,kwargs={'document_root':MEDIA_ROOT})
]


#django版本小于2.0的配置
# if DEBUG:
#     from django.views.static import serve
#     urlpatterns.append(path(r'media/(.*)',serve,kwargs={'document_root':MEDIA_ROOT}))