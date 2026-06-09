from django import forms
from .models import Students
class StudentRegistration(forms.Form):
    first_name= forms.CharField()
    last_name= forms.CharField()
    email= forms.EmailField()
    batch=forms.IntegerField()
    password= forms.CharField(widget=forms.PasswordInput())
    re_password= forms.CharField(widget=forms.PasswordInput())
    
    textarea=forms.CharField(widget=forms.Textarea())

    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match :
            raise forms.ValidationError("password doesn't match")


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
            "email": forms.EmailInput(attrs={"class": "form-input"}),
            "phone": forms.TextInput(attrs={"class": "form-input"}),
            "roll": forms.TextInput(attrs={"class": "form-input"}),
            "registration_no": forms.TextInput(attrs={"class": "form-input"}),
            "department": forms.Select(attrs={"class": "form-input"}),
            "semester": forms.Select(attrs={"class": "form-input"}),
            "date_of_birth": forms.DateInput(attrs={"class": "form-input", "type": "date"}),
            "address": forms.Textarea(attrs={"class": "form-input", "rows": 3}),
        }