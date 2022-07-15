from django.db import models
from django.contrib.auth.models import User



class Contact(models.Model):
    name = models.CharField("Full Name", max_length=200, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    subject = models.CharField("Subject", max_length=400, blank=True, null=True)
    message = models.TextField('Message', blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"


    def __str__(self):
        return f"{self.name} [ {self.email} ]"




class ContactAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    contact = models.CharField('Contact', max_length=15)
    location = models.CharField('Location', max_length=200)
    address = models.CharField('Address', max_length=200, default='')
    twitter = models.URLField("Twitter")
    facebook = models.URLField("Facebook")
    instagram = models.URLField("Instagram")
    linkedin = models.URLField("LinkedIn")
    description = models.TextField('Description', blank=True)


    class Meta:
        verbose_name = "Contact Administration"
        verbose_name_plural = "Contact Administration"

    def __str__(self):
        return str(self.user)


class Subscription(models.Model):
    mail = models.EmailField('Email', blank=True)

    def __str__(self):
        return self.mail
