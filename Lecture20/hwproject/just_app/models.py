import re
from django.core.validators import EmailValidator,RegexValidator,MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    gender = models.TextField()
    login = models.CharField(max_length=25, validators=[
        RegexValidator(
            regex=r"^[a-zA-Z0-9]{6,25}$",
            message = 'Login entered incorrectly!',
            code='Invalid login',
            inverse_match= False,
            flags=re.IGNORECASE
        )
    ])
    email = models.TextField(max_length=50, validators=[
        EmailValidator(
            message='Enter correct email!'
        )
    ])
    date_register = models.DateField()

    def __str__(self) -> str:
        return f'{self.first_name},{self.last_name}'

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_title = models.TextField()

    def __str__(self) -> str:
        return f'{self.category_title}'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=False)
    date_create = models.DateField()
    content = models.TextField(max_length=140)
    post_author_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.title},{self.date_create},{self.post_category_id}'
