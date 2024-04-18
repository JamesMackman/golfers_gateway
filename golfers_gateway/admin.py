from django.contrib import admin
from .models import GolfersProfile, GolfClub

# Register your models here.
@admin.register(GolfersProfile)
class GolfersProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'handicap')
    search_fields = ('user__username', 'bio')

@admin.register(GolfClub)
class GolfClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_latitude', 'location_longitude', 'rating')
    search_fields = ('name', 'description')