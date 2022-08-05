from multiprocessing import context
from django.shortcuts import render

from mainapp.models import HeaderCarousel, Student
from .forms import RegisterForm


def mainview(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.data.get("name")
            email = form.data.get("email")
            course = form.data.get("course")
            Student.objects.create(name=name, email=email, course=course)
    ads = HeaderCarousel.objects.all()[:3]
    for ad in ads:
        ad_title = ad.title[:5]
    form = RegisterForm()      
    context = {
        "form":form,
        "ads":ads,
             }
    return render(request, 'index.html', context=context)

def aboutview(request):
    return render(request, 'about.html')