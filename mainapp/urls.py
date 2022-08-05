from django.urls import path
from mainapp.views import mainview


urlpatterns = [
    path('', mainview),
]