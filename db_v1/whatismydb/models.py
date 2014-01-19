from django.db import models

# Abstract base class for representing time+value in database
class TimeValue(models.Model):
	time = models.DateTimeField('date/time recorded')
	value = models.FloatField()

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'\nValue: %s \nTime: %s\n' % (self.value, self.time)

	def save_object(self):
		save()

# Represents data collected every minute, subclass of TimeValue
class MinuteData(TimeValue):
	pass

# Represents data collected every hour, subclass of TimeValue
class HourData(TimeValue):
	pass

# Represents data collected every day, subclass of TimeValue
class DayData(TimeValue):
	pass