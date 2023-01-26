from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
         'class': 'form-control',
       
    }))
    

    class Meta:
        model = User
        fields = ['first_name','last_name','phone','email','username','password',]


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Dark'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nepal'
        self.fields['phone'].widget.attrs['placeholder'] = '9827155429'
        self.fields['email'].widget.attrs['placeholder'] = 'maildeepeshmahato@gmail.com'
        self.fields['username'].widget.attrs['placeholder'] = 'DarkNepal'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')


        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )