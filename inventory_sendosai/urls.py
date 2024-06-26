"""
URL configuration for inventory_sendosai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import HomeView, TestView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

prefix = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('test/', TestView.as_view(), name='docs-test'),
    path(prefix+'inventory/', include('inventory_api.urls')),
    path(prefix+'auth/', include('accounts_api.urls')),
    path(prefix+'schema/', SpectacularAPIView.as_view(), name='schema'),
    path(prefix+'docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path(prefix+'docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
