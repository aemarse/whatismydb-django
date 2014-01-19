from django.shortcuts import render, get_list_or_404

from whatismydb.models import MinuteData, HourData, DayData, TimeIntervals, QueryData

def home(request):
	# Queryset for getting all objects, ordered by time
	min_data = MinuteData.objects.order_by('time')
	
	# Get the objects as a list
	all_minute_data = get_list_or_404(min_data)

	# Queryset for time intervals
	time_interval_choices = TimeIntervals.time_interval_choices
	# time_interval_choices = QueryData.time_intervals

	# Start time
	

	# End time
	

	# Map template var name to Python obj
	context = {'all_minute_data': all_minute_data,
				'choices': time_interval_choices,}

	# Render the page!
	return render(request, 'whatismydb/home.html', context)

