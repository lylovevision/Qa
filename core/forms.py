from django import forms
from django.contrib.auth import get_user_model


class UserForm(forms.ModelForm):
    password = forms.CharField(label='请输入密码', widget=forms.PasswordInput()) 

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
