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
from .models import CompanyUser
from django import forms

class SignUpForm(UserCreationForm):
    company_username = forms.CharField(max_length=32, help_text='Введите логин компании')
    # TODO: Сделать автоматический перевод название компании в формате "общ. с огр. ответ. 'Лия' -> ООО 'Лия'"
    company_name = forms.CharField(max_length=63, help_text='Введите полное название компании.')
    director_post = forms.CharField(max_length=32, help_text='Введите должность руководителя компании', initial='Директор')
    director_last_name = forms.CharField(max_length=63, help_text='Введите фамилию руководителя компании')
    diretor_first_name = forms.CharField(max_length=63, help_text='Введите имя руководителя компании')
    director_patronymic = forms.CharField(max_length=63, help_text='Введите отчество руководителя компании')
    
    # TODO: Написать проверку пароля так, чтобы он проверялся через регулярное выражение
    class Meta:
        model = CompanyUser
        fields = ('company_username', 'company_name', 'director_post', 'director_last_name', 'diretor_first_name', 'director_patronymic', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин компании')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)