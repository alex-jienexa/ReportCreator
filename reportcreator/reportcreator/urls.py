"""
URL configuration for reportcreator project.

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
from django.urls import path, include
from pages import views as pages_views
from companies.views import signup_view, login_view
from documents.views import create_document, create_template, get_template_fields

urlpatterns = [
    path('docs/create/', create_document, name='create-document'),
    path('templates/create/', create_template, name='create-template'),
    path('api/get-template-fields/<int:template_id>/', get_template_fields, name='get-template-fields'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    #path('', pages_views.hello),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]
