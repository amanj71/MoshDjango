from django import forms

## write Form classes here
class ContactPageForm(forms.Form):
    fullname = forms.CharField(max_length=88, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Your Full Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control", "placeholder": "Your Email"
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control", "placeholder": "Your Content"
    }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "@yahoo.com" in email:
            raise forms.ValidationError("Enter Yahoo mail Pleas")
        return email
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords should match together")
        return data

