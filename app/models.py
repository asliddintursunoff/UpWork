from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=300)
    about = models.TextField(null=True,blank=True)

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = 'Bo\'lim '
        verbose_name_plural = 'Bo\'limlar '

class Worker(models.Model):
    bulim= models.ForeignKey(Organization, on_delete=models.CASCADE)
    FIO= models.CharField(max_length=200)
   
    specialty =models.CharField(max_length=1000)
    staffka = models.IntegerField()
    phone = models.CharField(max_length=13,help_text=" +998 bilan kiriting")

    class Meta:
        verbose_name = 'Ishchi '
        verbose_name_plural = 'Ishchilar  '

    def __str__(self) :
        return self.FIO
class Worker_about(models.Model):
    FIO = models.ForeignKey(Worker, on_delete=models.CASCADE)
    # last_name=  models.ForeignKey(Worker, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=200)
    birthday = models.DateField()
    information =models.CharField(max_length=200)
    graduated_university = models.CharField(max_length=1000,null=True,blank=True,help_text="if worker studied university , you can fill out this space,else not")
    magistratura = models.CharField(max_length=1000,null=True,blank=True,help_text="if worker studied magistratura , you can fill out this space,else not")
    know_languages = models.CharField(max_length=200)
    describtion = models.TextField(help_text="about worker")
    def __str__(self) :
        return f"{self.FIO}"
    
    class Meta:
        verbose_name = 'Ishchi malumoti '
        verbose_name_plural = 'Ishchilar malumoti '


class Relationship(models.Model):

    hodim = models.ForeignKey(Worker_about, on_delete=models.CASCADE)

    qarindoshligi = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")

    qarindosh_ismi = models.CharField(max_length=500, help_text="Qarindoshni kiriting.....")

    qarindosh_tug_yil = models.DateField()

    yashash_joyi = models.CharField(max_length=500, help_text="Yashash manzil...")

    ish_joyi = models.CharField(max_length=500, help_text="Ish manzil...")




    def __str__(self):

        return "hodim"

    class Meta:
        
        verbose_name = 'Qarindoshi'
        verbose_name_plural = 'Qarindoshlari'
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
   phone_number= models.CharField(max_length=12, unique=True)
   is_phone_verified = models.BooleanField(default=False)
   otp = models.CharField(max_length=6)

   USERNAME_FIELD = "phone_number"
   REQUIRED_FIELDS = []
   object = UserManager()
    