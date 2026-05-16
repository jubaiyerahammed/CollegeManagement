from django import forms

class StudentRegistration(forms.Form):
    first_name= forms.CharField()
    last_name= forms.CharField()
    email= forms.EmailField()
    batch=forms.IntegerField()
    password= forms.CharField(widget=forms.PasswordInput())
    textarea=forms.CharField(widget=forms.Textarea())
