from django import forms
from .models import Student
COURSE_CHOISE = (
    ('Course1','Course1'),
    ('Course2','Course2'),
    ('Course3','Course3'),
)


class RegisterForm(forms.Form):
    email = forms.EmailField( label="", initial='', widget = forms.EmailInput(attrs={"placeholder":"Your email", "id":"form3Example1c","class":"form-control border-0 p-4", "required":"required"}))
    name = forms.CharField( label="", initial='', widget = forms.TextInput(attrs={"placeholder":"Your name","id":"form3Example1c","class":"form-control border-0 p-4", "required":"required"}))
    course = forms.ChoiceField(choices = COURSE_CHOISE, label="", initial='', widget = forms.Select(attrs={"placeholder":"Select a course","id":"form3Example4cd","class":"custom-select border-0 px-4"}))
    


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'course')
        widgets = {
            'name': forms.TextInput(attrs={"placeholder":"Your name","id":"form3Example1c","class":"form-control border-0 p-4", "required":"required"}),
            'email':forms.EmailInput(attrs={"placeholder":"Your email", "id":"form3Example1c","class":"form-control border-0 p-4", "required":"required"}),
            'course':forms.Select(attrs={"placeholder":"Select a course","id":"form3Example4cd","class":"custom-select border-0 px-4"})
        }