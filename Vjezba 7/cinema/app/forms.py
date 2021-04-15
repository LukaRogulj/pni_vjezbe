from django import forms
from .models import Projection, Ticket
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import request

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Projection
        fields = ['movieName', 'cinemaHallCapacity', 'screeningTime']

class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        #exclude = ['customer']
        fields = ['movieName', 'customer', 'seatNumber']

class BuyTicketForm(forms.ModelForm):
    class Meta:
        model = Projection
        fields = ['movieName', 'cinemaHallCapacity']

