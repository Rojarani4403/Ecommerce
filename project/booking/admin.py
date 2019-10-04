from django.contrib import admin

# Register your models here.
from .models import Booking,Movie,Show,Seat,BookedSeat,Theatre

from .models import country,state,City
class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking,BookingAdmin)

class ShowAdmin(admin.ModelAdmin):
	class Meta:
		model = Show

admin.site.register(Show,ShowAdmin)

class MovieAdmin(admin.ModelAdmin):
	class Meta:
		model = Movie

admin.site.register(Movie,MovieAdmin)

class SeatAdmin(admin.ModelAdmin):
	class Meta:
		model = Seat
admin.site.register(Seat,SeatAdmin)

class BookedSeatAdmin(admin.ModelAdmin):
	class Meta:
		model = BookedSeat

admin.site.register(BookedSeat,BookedSeatAdmin)

class TheatreAdmin(admin.ModelAdmin):
	class Meta:
		model = Theatre

admin.site.register(Theatre,TheatreAdmin)

class CountryAdmin(admin.ModelAdmin):
	list_display = ('country_name',)
	fields = ('country_name',)
	ordering = ('country_name',)
admin.site.register(country,CountryAdmin)
#
class StateAdmin(admin.ModelAdmin):
	list_display = ('state_name','country_field',)
	fields = ('state_name','country_field')
	ordering = ('country_field',)
admin.site.register(state,StateAdmin)
#

class CityAdmin(admin.ModelAdmin):
	list_display = ('city_name','state',)
	fields = ('city_name','state')
	ordering = ('state',)
	search_fields = ('state',)

admin.site.register(City,CityAdmin)
