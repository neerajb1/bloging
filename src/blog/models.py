from django.db import models

# Create your models here.

class SignUp(models.Model):
    email =  models.EmailField()
    full_name = models.CharField(max_length = 120 , blank = True , null = True)
    timestamp = models.DateField(auto_now_add = True , auto_now = False)
    updated = models.DateField(auto_now_add= False , auto_now = True)
    #auto_now_add --> when first time created
    #auto_now  --> update each time

    def __str__(self):
        return self.email
