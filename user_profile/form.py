from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user_profile.models import Profile
from django import forms 

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit: 
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('dob',)