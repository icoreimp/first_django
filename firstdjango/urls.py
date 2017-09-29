"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from inventory.views import IndexView, ItemDetailsView, ItemAdd1View, ItemAdd2View, ItemAdd4View, ItemAdd3View

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'item/(?P<id>\d+)/$',ItemDetailsView.as_view(),name='item_details'),
    url(r'add-item1/$',ItemAdd1View.as_view(),name='item_add1'),
    url(r'add-item2/$',ItemAdd2View.as_view(),name='item_add2'),
    url(r'add-item3/$',ItemAdd3View.as_view(),name='item_add3'),
    url(r'add-item4/$',ItemAdd4View.as_view(),name='item_add4'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
