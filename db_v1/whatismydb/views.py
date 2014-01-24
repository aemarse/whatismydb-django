from django.shortcuts import render, get_list_or_404
from datetime import datetime
from time import mktime

from whatismydb.models import MinuteData, HourData, DayData, TimeIntervals, QueryData

def home(request):

	# Make sure "Get Data" form parameters are set
	if request.GET.get('start_time') and request.GET.get('end_time') and request.GET.get('time_intervals'):
		
		# GET parameters from the request
		time_interval = request.GET.get('time_intervals')
		start_time = request.GET.get('start_time')
		end_time = request.GET.get('end_time')

		# Convert from DateTime to timestamp
		# start_time = mktime(start_time.timetuple())+1e-6*start_time.microsecond
		# end_time = mktime(end_time.timetuple())+1e-6*end_time.microsecond

		# Get objects from the requested database table
		if time_interval == 'Minute':
			data_objects = MinuteData.objects.order_by('timestamp')
		elif time_interval == 'Hour':
			data_objects = HourData.objects.order_by('timestamp')
		elif time_interval == 'Day':
			data_objects = DayData.objects.order_by('timestamp')

	else:
		# Add error message to form

		# Get some data from the MinuteData table
		data_objects = MinuteData.objects.order_by('timestamp')[:10]

	# Get the objects as a list
	data_list = get_list_or_404(data_objects)

	# Convert from Unix timestamp to DateTime format
	date_time = getDateTime(data_list)

	# Queryset for time intervals
	time_interval_choices = TimeIntervals.time_interval_choices

	# Earliest and latest data
	earliest = datetime.fromtimestamp(data_objects[0].timestamp)
	latest = datetime.fromtimestamp(data_objects[len(data_objects)-1].timestamp)

	# Chart data
	xdata = [1, 2, 3, 4, 5]
	# ydata = [1, 2, 3, 4, 5]
	# xdata = data_objects.values_list('timestamp')
	ydata = data_objects.values_list('value')

	chartdata = {'x': xdata, 'y': ydata}
	charttype = "lineChart"
	chartcontainer = 'linechart_container'

	# Map template var name to Python obj
	context = {'date_time': date_time,
				'choices': time_interval_choices,
				'earliest': earliest,
				'latest': latest,
				'charttype': charttype,
    			'chartdata': chartdata,
    			'chartcontainer': chartcontainer,
    			'extra': {
        			'x_is_date': False,
        			'x_axis_format': '',
        			'tag_script_js': True,
        			'jquery_on_ready': False,
        		}
        	}

	# Render the page!
	return render(request, 'whatismydb/home.html', context)

# HELPER FUNCTIONS
def getDateTime(data_list):
	for index in range(len(data_list)):
		data_list[index].timestamp = datetime.fromtimestamp(data_list[index].timestamp)
	return data_list
