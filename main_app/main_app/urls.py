"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from avito2_0 import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('bio', views.member_bio, name='mem_bio'),
    path('add_item', views.add_item, name='add_item'),
    path('registration', views.registration, name='reg'),
    path('redaction', views.redaction, name='redact'),
    path('logout', views.logout, name='logout'),
    path(r'^single/(?P<id>\w+)$', views.single, name='single'),
    path(r'cart', views.cart, name='cart'),
    path(r'^add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path(r'make_order', views.make_order, name='make_order')
]
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
