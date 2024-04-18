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

class Booking(models.Model):
    golfer = models.ForeignKey(GolfersProfile, on_delete=models.CASCADE)
    tee_time = models.ForeignKey(TeeTime, on_delete=models.CASCADE)
    booking_date_and_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')])
    guests_count = models.PositiveIntegerField(default=1)

class Review(models.Model):
    golfer = models.ForeignKey(GolfersProfile, on_delete=models.CASCADE)
    golf_club = models.ForeignKey(GolfClub, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    # Fields for reviewer information
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()

class Membership(models.Model):
    golfer = models.ForeignKey(GolfersProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('expired', 'Expired')])
    membership_number = models.CharField(max_length=20)  
    benefits = models.TextField(blank=True)
    fees = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    renewal_required = models.BooleanField(default=True)
    renewal_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)