#เลขาของห้อง myapp

from django.urls import path
from .views import homepage

urlpatterns = [
    path('', homepage), #localhost:8000/ www.loog.com
]