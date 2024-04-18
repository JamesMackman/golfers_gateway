from django.contrib import admin
from .models import GolfersProfile, GolfClub

# Register your models here.
@admin.register(GolfersProfile)
class GolfersProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'handicap')
    list_filter = ('handicap',)
    search_fields = ('user__username', 'bio')

@admin.register(GolfClub)
class GolfClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_latitude', 'location_longitude', 'rating')
    search_fields = ('name', 'description', 'contact_information')

@admin.register(TeeTime)
class TeeTimeAdmin(admin.ModelAdmin):
    list_display = ('golf_club', 'date_and_time', 'price', 'available_slots')
    list_filter = ('golf_club', 'date_and_time')
    search_fields = ('golf_club__name',)