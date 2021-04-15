from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Projection(models.Model):
    movieName = models.TextField()
    screeningTime = models.IntegerField()
    cinemaHallCapacity = models.IntegerField(default=20)

    # class Meta:
    #     ordering = ["-movieName"]

    def __str__(self):
        return self.movieName
        
    def get_absolute_url(self):
        return reverse('projection-detail', kwargs={'pk':self.pk})

class Ticket(models.Model):
    seatNumber = models.IntegerField(null=True)
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    movieName = models.ForeignKey(Projection, on_delete = models.CASCADE, null=True)

    # def __str__(self):
    #     return self.seatNumber

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk':self.pk})
