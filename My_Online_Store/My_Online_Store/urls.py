"""My_Online_Store URL Configuration

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
from django.urls import path, include
from products.views import ProductListView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import cart_view, checkout_view, processOrder, thankyou, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/list/', ProductListView.as_view()),
    path('products/', include('products.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('process_order/', processOrder, name="process_order"),
    path('register/', register_view, name="register"),
    path('thankyou/<int:id>', thankyou, name="thankyou"),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)