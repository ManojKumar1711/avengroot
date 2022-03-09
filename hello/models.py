from django.db import models

# Create your models here. This is a blueprint of the database that we create.
# the table will be created with the name hello_Contact


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name
