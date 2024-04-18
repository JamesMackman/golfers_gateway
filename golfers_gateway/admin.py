from django.contrib import admin
from .models import GolfersProfile, GolfClub, TeeTime, Booking, Review, Membership 

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

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('golfer', 'tee_time', 'booking_date_and_time', 'status', 'guests_count')
    list_filter = ('status',)
    search_fields = ('golfer__user__username',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('golfer', 'golf_club', 'rating', 'date', 'reviewer_name', 'reviewer_email')
    list_filter = ('rating',)
    search_fields = ('golfer__user__username', 'golf_club__name', 'reviewer_name', 'reviewer_email')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('golfer', 'start_date', 'end_date', 'membership_type', 'status', 'membership_number', 'benefits', 'fees', 'renewal_required', 'renewal_fee')
    list_filter = ('status', 'membership_type', 'renewal_required')
    search_fields = ('golfer__user__username', 'membership_number', 'benefits')