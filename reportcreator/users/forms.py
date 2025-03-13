"""
Форма аутентификации пользователя в систему.
У модели пользователя, как объекта аутентификации в систему, имеются следующие поля:
- `username` - имя пользователя, под которм он входит в систему. 
Должно быть уникальным в рамках всей системы.
Максимальная длина имени - 150 символов.
Может содержать цифры, буквы, символы "@", ".", "+", "-" и "_".
Является ключевым полем для связи с `models.User`.
- `email` - адрес электронной почты, к которому будет привязан пользователь.
Соостветствие правильности происходит с помощью средств Django (`models.EmailField`).
- `password` - пароль пользователя.
Максимальная длина пароля - 128 символов.

Все данные о пользователях сохраняются в базе данных `auth_user`?
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)