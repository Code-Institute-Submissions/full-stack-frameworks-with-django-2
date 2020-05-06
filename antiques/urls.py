"""antiques URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from home import urls as urls_home
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from contact import urls as urls_contact
from django.views import static
from .settings import MEDIA_ROOT
from django.conf import settings


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', include('home.urls')),
    path(r'products/', include('products.urls')),
    path(r'cart/', include('cart.urls')),
    path(r'accounts/', include('accounts.urls')),
    path(r'search/', include('search.urls')),
    path(r'checkout/', include('checkout.urls')),
    path(r'contact/', include('contact.urls')),
    path(r'media/(<path>.*)', static.serve, {'document_root': MEDIA_ROOT}),
]
