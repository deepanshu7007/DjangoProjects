from django.db import models

class UserLogin(models.Model):
    UserName = models.CharField(max_length=50);
    Passwords = models.CharField(max_length=50);
    
def __str__(self):
    return self.UserName;
