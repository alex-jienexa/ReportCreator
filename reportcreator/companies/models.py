from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import random

class Company(models.Model):
    """
    Базовая абстрактная модель компании, от которой будут наследоваться другие модели.

    Здесь определены базовые поля, которые имеются как в Исполнителе, так и в 
    Заказчике, такие как:
    - Уникальный идентификационный номер компании (создаётся автоматически)
    - Название компании
    - Полное название компании с расшифровкой всех абревиатур
    - Название должности, от имени которого осуществляется подпись документа
    - ФИО должности, от чьего имени осуществляется подпись документа
    - Инициалы ФИО руководителя компании. TODO: сделать его автовычислимым согласно скрипту (ФАМИЛИЯ И. О.)
    """
    class Meta:
        abstract = True
    
    company_username = models.CharField(max_length=32, verbose_name='Логин', primary_key=True, default=f"company{random.randint(0, 1000)}")
    company_name = models.CharField(max_length=64)
    company_fullName = models.CharField(max_length=256, null=False, default=company_name)
    director_post = models.CharField(max_length=32, default='Директор', verbose_name='Должность директора')
    director_last_name = models.CharField(max_length=63, null=True, verbose_name='Фамилия директора')
    diretor_first_name = models.CharField(max_length=63, null=True, verbose_name='Имя директора')
    director_patronymic = models.CharField(max_length=63, null=True, verbose_name='Отчество директора')

    def __str__(self):
        return self.company_name

class CompanyUser(AbstractBaseUser, PermissionsMixin):
    """
    Базовая абстрактная модель компании, от которой будут наследоваться другие модели.

    Здесь определены базовые поля, которые имеются как в Исполнителе, так и в 
    Заказчике, такие как:
    - Уникальный идентификационный номер компании (создаётся автоматически)
    - Название компании
    - Полное название компании с расшифровкой всех абревиатур
    - Название должности, от имени которого осуществляется подпись документа
    - ФИО должности, от чьего имени осуществляется подпись документа
    - Инициалы ФИО руководителя компании. TODO: сделать его автовычислимым согласно скрипту (ФАМИЛИЯ И. О.)
    """

    USERNAME_FIELD = 'company_username'
    
    company_username = models.CharField(max_length=32, verbose_name='Логин', primary_key=True, default=f"company{random.randint(0, 1000)}", unique=True)
    company_name = models.CharField(max_length=64)
    company_fullName = models.CharField(max_length=256, null=False, default=company_name)
    director_post = models.CharField(max_length=32, default='Директор', verbose_name='Должность директора')
    director_last_name = models.CharField(max_length=63, null=True, verbose_name='Фамилия директора')
    diretor_first_name = models.CharField(max_length=63, null=True, verbose_name='Имя директора')
    director_patronymic = models.CharField(max_length=63, null=True, verbose_name='Отчество директора')

    def __str__(self):
        return self.company_name

class Executor(Company):
    """
    Модель компании исполнителя. 
    Наследует все поля из Company.

    TODO: Добавляет ли он дополнительные поля?
    """

class Contractor(Company):
    """
    Модель компани-заказчика.
    Наследует все поля из Company, а также добавляет:
    - Город-месторасположение компании, где происходит подпись документа.
    """
    contractor_city = models.CharField(max_length=64, null=False)