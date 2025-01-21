"""
URL configuration for diplom_django project.

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
from diplom_dj_app.views import main_page_f
from diplom_dj_app.views import shop_page_f
from diplom_dj_app.views import cart_page_f
from diplom_dj_app.views import sign_up_by_django
from diplom_dj_app.views import enter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_page_f),
    path('main_page/shop_page/', shop_page_f),
    path('main_page/cart_page/', cart_page_f),
    path('main_page/registration/', sign_up_by_django),
    path('main_page/enter/', enter)
]
