"""stepik_tours URL Configuration

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
from django.urls import path

from tours.views import main_view
from tours.views import departure_view
from tours.views import tour_view
from tours.views import custom_handler404, custom_handler500

urlpatterns = [
    path('', main_view),
    path('departure/<str:departure>', departure_view),
    path('tour/<int:tour_id>', tour_view),
]

handler500 = custom_handler500
handler404 = custom_handler404
