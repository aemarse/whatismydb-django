from django.contrib import admin
from whatismydb.models import MinuteData, HourData, DayData

class TimeValueAdmin(admin.ModelAdmin):

	fieldsets = [
        ('Timestamp', {'fields': ['timestamp']}),
        ('Value', {'fields': ['value']}),
    ]

	list_display = ('timestamp', 'value')
	list_filter = ['timestamp', 'value']

	class Meta:
		abstract = True

class MinuteDataAdmin(TimeValueAdmin):
	pass

class HourDataAdmin(TimeValueAdmin):
	pass

class DayDataAdmin(TimeValueAdmin):
	pass

admin.site.register(MinuteData, MinuteDataAdmin)
admin.site.register(HourData, HourDataAdmin)
admin.site.register(DayData, DayDataAdmin)