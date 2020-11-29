"""djangobookapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from accounts.views import login
from home.views import index
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import path 
from django.conf.urls.static import static
from accounts.views import register, login, profile
from django.urls import include, re_path
from products import urls as products_urls
from billing.views import purchase_product


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', index,name='index' ),
    path('advertise_costs/',TemplateView.as_view(template_name="advertise_costs.html"), name='advertise_costs'),
    path('advertise/',TemplateView.as_view(template_name="advertise.html"), name='advertise'),
    path('aboutus/',TemplateView.as_view(template_name="aboutus.html"), name='aboutus'),
    path('about-the-authors/',TemplateView.as_view(template_name="about-the-authors.html"), name='about-authors'),
    path('register/',register, name='register'),
    path('profile/',profile, name='profile'),
    path('login/',login, name='login'),
    path('product/', include(products_urls)),
    path('purchase_product/',purchase_product, name='purchase_product'),
    path('yearly_subscription/',TemplateView.as_view(template_name="yearly_subscription.html"), name='yearly_subscription'),
    path('monthly_subscription/',TemplateView.as_view(template_name="monthly_subscription.html"), name='monthly_subscription'),
    
   
]
