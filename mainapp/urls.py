from django.urls import path
from mainapp.views import aboutview, mainview


urlpatterns = [
    path('', mainview, name='mainview'),
    path('about/', aboutview, name='aboutview')
]