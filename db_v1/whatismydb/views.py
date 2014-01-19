from django.shortcuts import render, get_list_or_404

from whatismydb.models import MinuteData, HourData, DayData

def home(request):
	# Queryset for getting all objects, ordered by time
	filt_data = MinuteData.objects.order_by('time')
	
	# Get the objects as a list
	all_minute_data = get_list_or_404(filt_data)

	# Map template var name to Python obj
	context = {'all_minute_data': all_minute_data}

	# Render the page!
	return render(request, 'whatismydb/home.html', context)