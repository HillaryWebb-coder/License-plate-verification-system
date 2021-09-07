from django.urls import path
from .views import CreateLog

urlpatterns = [
    path('', CreateLog, name='Upload')
]