from django.db import models
import random
import string
# Create your models here


class Transfer(models.Model):
    ext_id = models.CharField()
    receiver_card_number = models.CharField()
    sender_card_number = models.CharField()
    otp = models.CharField(help_text="6-digit OTP code sent for confirmation")
   


    class Meta:
        ordering = ['ext_id']
        verbose_name = 'Transfer'
        verbose_name_plural ='Transfers'