"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from hello.baseline_data import add_to_cart
from hello.views import IndexView, LoginView, RegisterView, CatalogView, CartView, ProductView, AdminView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="home"),
    path('catalog/', CatalogView.as_view(), name="catalog"),
    path('cart/', CartView.as_view(), name="cart"),
    path('product/<str:name>/', ProductView.as_view(), name='product'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('siteadmin/', AdminView.as_view(), name='siteadmin'),
    path('cart/remove/<int:item_id>/', CartView.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:weapon_id>/', add_to_cart, name='add_to_cart')
]
urlpatterns += staticfiles_urlpatterns()


