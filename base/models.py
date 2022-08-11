from django.db import migrations, models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):   # Custom class
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)  # Name the record using name of the record

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    updated = models.DateTimeField(auto_now=True)  #Update each time update the record - Date and time
    created = models.DateTimeField(auto_now_add=True) #Update only the initial created - Date and time

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return str(self.name)  # Name the record using name of the record

class Message(models.Model):     # Create a relationship - Custom class
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  #Update each time update the record - Date and time
    created = models.DateTimeField(auto_now_add=True) #Update only the initial created - Date and time

    def __str__(self):
        return self.body[0:50]  # Name the record using name of the record