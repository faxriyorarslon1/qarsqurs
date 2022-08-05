from multiprocessing import context
from django.shortcuts import render

from mainapp.models import Student
from .forms import RegisterForm


def mainview(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # print("salomndigiodiofgfdogjfogfjdgfkdgfnodfhfpfnhpodfdfh", form.data.get('course'))
        if form.is_valid():
            name = form.data.get("name")
            email = form.data.get("email")
            course = form.data.get("course")
            Student.objects.create(name=name, email=email, course=course)
    form = RegisterForm()      
    context = {
        "form":form,
                    }
    return render(request, 'index.html', context=context)

def aboutview(request):
    return render(request, 'about.html')