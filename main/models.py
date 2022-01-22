from ast import Index
from audioop import reverse
from operator import index
from pydoc import describe
from statistics import mode
from tkinter import CASCADE
from turtle import title
from unicodedata import name
from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=64)
    img = models.ImageField()
    def __str__(self):
        return self.name    
    
class Player_roll(models.Model):
    name = models.CharField(max_length=64)
    palyer = models.ManyToManyField('Player')   
    def __str__(self):
        return self.name    
class Player(models.Model):
    nikname = models.CharField(max_length=64)
    def __str__(self):
        return self.nikname    

    
class War(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    players = models.ForeignKey(Player_roll, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    vidio = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse("war", kwargs={"War_slug": self.slug})
    
class News(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title    
    def get_absolute_url(self):
        return reverse("war", kwargs={"news_slug": self.slug})
    
class Event(models.Model):
    name = models.CharField(max_length=64)
    describtion = models.TextField()
    start = models.DateTimeField()
    registaration_finish = models.DateTimeField()
    price = models.CharField(max_length=64, null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, auto_created=True, db_index=True)
    
    def __str__(self):
        return self.name    
    
    def get_absolute_url(self):
        return reverse("evente", kwargs={"event_slug": self.slug})