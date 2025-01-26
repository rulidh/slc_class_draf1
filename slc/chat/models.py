from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)  # Nama user
    user_fullname = models.CharField(max_length=100)
    user_email = models.EmailField()             # Email user
    password = models.CharField(max_length=20)
    user_number = models.DecimalField(max_digits=12, decimal_places=2)
    user_photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.username  # Menampilkan username saat objek dipanggil
