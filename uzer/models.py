from django.db import models
from django.contrib.auth.models import AbstractUser


class UzerModel(AbstractUser):
    img = models.ImageField(upload_to='uzers/')

# Create your models here.
