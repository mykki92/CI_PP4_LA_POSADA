from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking


# Registration of the table model in the admin panel
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_number', 'seats')


# Registration of the booking model in the admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'party_of',
        'status',
        'table_id',
        'booking_date',
        'booking_time',
        'created_on'
    )
    list_display = (
        'booking_id',
        'user',
        'name',
        'phone',
        'party_of',
        'status',
        'table',
        'booking_date',
        'booking_time',
        'created_on'
    )

    search_fields = ['guest__name']
    list_filter = (('booking_date', DateRangeFilter),)
    actions = ['confirm_booking', 'reject_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(status='Confirmed')

    def reject_booking(self, request, queryset):
        queryset.update(status='Rejected')
