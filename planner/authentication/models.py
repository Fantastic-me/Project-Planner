from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractUser

class RoleChoice(models.TextChoices):

    ADMIN='Admin','Admin'

    COORDINATOR='Project Coordinator','Project Coordinator'

    DEVELOPER='Developer','Developer'


class TechChoices(models.TextChoices):

    BACKEND='Backend Developer','Backend Developer'

    FRONDEND='Frondend Developer','Frondend Developer'

    FULLSTACK='Fullstack Developer','Fullstack Developer'

    UI_UX='UI/UX Designer','UI/UX Designer'

    TESTER='Software Tester','Software Tester'

class Profile(AbstractUser):

    role=models.CharField(max_length=30,choices=RoleChoice.choices)

    tech=models.CharField(max_length=30,choices=TechChoices.choices,null=True,blank=True)

    class Meta:

        verbose_name='Profiles'

        verbose_name_plural='Profiles'

    def __str__(self):

        return f'{self.first_name}-{self.tech}'



