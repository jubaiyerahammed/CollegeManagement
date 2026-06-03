from django import forms

class StudentRegistration(forms.Form):
    first_name= forms.CharField()
    last_name=forms.CharField()
    email= forms.EmailField()
    batch= forms.IntegerField()
    
    password= forms.CharField(widget=forms.PasswordInput())
    re_password= forms.CharField(widget=forms.PasswordInput())


    textarea= forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data= super().clean()
        password_match=self.cleaned_data['password']
        re_password_match=self.cleaned_data['re_password']
        if password_match!=re_password_match:
            raise forms.ValidationError("password doesn't match")
