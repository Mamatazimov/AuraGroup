from django.db import models

# Create your models here.

class Member(models.Model):
    full_name = models.CharField()
    workplace = models.CharField()
    photo = models.ImageField(upload_to='member_photo/')
    bio = models.TextField()

    def __str__(self):
        return f"{self.full_name}'s profile"





