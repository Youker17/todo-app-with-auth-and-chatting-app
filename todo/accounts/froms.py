from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Profile




class CreatingUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="email")
    username = forms.CharField(required=True,label="username",min_length=5, max_length=15)
    password1 = forms.CharField(required=True,label="password")
    password2 = forms.CharField(required=True,label="confirm password")


    def username_clean(self):
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise Exception.ValidationError("User Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise Exception.ValidationError(" Email Already Exist")  
        return email
    
    def clean_password2(self) -> str:
        return super().clean_password2()
    

    def save(self, commit=True):
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )
        pro = Profile(user=user)
        pro.save()
        return user


    # def confirm_pass(self):
    #     if self.password1 == self.password2:
    #         return True
    #     return False
    
    # def exists(self):
        


