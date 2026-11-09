from django.urls import path
from .views import login_view , csrf_view

urlpatterns = [
    path('login/', login_view, name='login'),
     path('csrf/', csrf_view),
]