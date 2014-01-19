from django.db import models
from django.forms import ModelForm

# Abstract base class for representing time+value in database
class TimeValue(models.Model):
	time = models.DateTimeField('date/time recorded')
	value = models.FloatField()

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'\nValue: %s \nTime: %s\n' % (self.value, self.time)

# Represents data collected every minute, subclass of TimeValue
class MinuteData(TimeValue):
	pass

# Represents data collected every hour, subclass of TimeValue
class HourData(TimeValue):
	pass

# Represents data collected every day, subclass of TimeValue
class DayData(TimeValue):
	pass

class TimeIntervals(models.Model):
	time_interval_choices = (
	'Minute',
	'Hour',
	'Day',
	)

# Query choices for "get" form
class QueryData(models.Model):
	date_time = models.DateTimeField()
	time_intervals = models.ForeignKey(TimeIntervals)

# Update rate choices for "get" form
class QueryDataForm(ModelForm):
	class Meta:
		model = QueryData
		fields = ['date_time', 'time_intervals']


