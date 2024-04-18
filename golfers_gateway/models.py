from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GolfersProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    handicap = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    favorite_courses = models.ManyToManyField('GolfClub', blank=True)

class GolfClub(models.Model):
    name = models.CharField(max_length=100)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    image = models.ImageField(upload_to='golf_club_images/')
    contact_information = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)

class TeeTime(models.Model):
    golf_club = models.ForeignKey(GolfClub, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_slots = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()  
    booking_open_date = models.DateField()  
    booking_close_date = models.DateField()

