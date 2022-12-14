from distutils.command.upload import upload
from django.db import models

COURSE_CHOISE = [
    ('Course1','Course1'),
    ('Course2','Course2'),
    ('Course3','Course3'),
]


class Student(models.Model):
    name =models.CharField(max_length=15)
    email = models. EmailField(max_length=30)
    course = models.CharField(max_length=30, choices=COURSE_CHOISE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"


class HeaderCarousel(models.Model):
    title  = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media/header_carousel/')

    def __str__(self):
        return self.theme
    
    class Meta:
        verbose_name = "Reklama"
        verbose_name_plural = "Reklamalar"




