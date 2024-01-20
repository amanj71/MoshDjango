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