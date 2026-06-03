from django import forms

# class StudentRegistration(forms.Form):
#     first_name= forms.CharField()
#     last_name=forms.CharField()
#     email= forms.EmailField()
#     batch= forms.IntegerField()
    
#     password= forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20, error_messages={
#             "min_length": "Password must be at least 8 characters",
#             "max_length": "Password cannot exceed 20 characters"
#         })
#     re_password= forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=20)


#     textarea= forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         cleaned_data= super().clean()
#         password_match=self.cleaned_data['password']
#         re_password_match=self.cleaned_data['re_password']
#         if password_match!=re_password_match:
#             raise forms.ValidationError("password doesn't match")
#         return cleaned_data
class StudentRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    batch = forms.IntegerField()

    password = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=20,
        error_messages={
            "min_length": "Password must be at least 8 characters",
            "max_length": "Password cannot exceed 20 characters"
        }
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=20
    )

    textarea = forms.CharField(widget=forms.Textarea (attrs={'rows':4, 'cols':20}))
    payments= forms.DecimalField(min_value=5000, max_value=10000, max_digits=7, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        # Password match check
        if password and re_password and password != re_password:
            raise forms.ValidationError("password doesn't match")

        return cleaned_data
