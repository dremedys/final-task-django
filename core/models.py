from django.conf import settings
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, BaseUserManager
from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=30)


class Journal(BookJournalBase):
    class Type(models.TextChoices):
        BULLET = 'BL', 'Bullet',
        FOOD = 'FD', 'Food',
        TRAVEL = 'TR', 'Travel'
        SPORT = 'SP', 'Sport'

    type = models.CharField(max_length=2, choices=Type.choices, default=Type.BULLET)
    publisher = models.CharField(max_length=50)


class UserProfile(AbstractUser):
    is_super = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)