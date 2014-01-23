from django.shortcuts import render, get_list_or_404

from whatismydb.models import MinuteData, HourData, DayData, TimeIntervals, QueryData

def home(request):

	# Make sure "Get Data" form parameters are set
	if request.GET.get('start_time') and request.GET.get('end_time') and request.GET.get('time_intervals'):
		
		# GET parameters from the request
		time_interval = request.GET.get('time_intervals')
		start_time = request.GET.get('start_time')
		end_time = request.GET.get('end_time')

		# Get objects from the requested database table
		if time_interval == 'Minute':
			data_objects = MinuteData.objects.order_by('time')
		elif time_interval == 'Hour':
			data_objects = HourData.objects.order_by('time')
		elif time_interval == 'Day':
			data_objects = DayData.objects.order_by('time')

		# Get the proper data for visualization and table
		xdata = [1, 2, 3, 4, 5] # data_objects.values_list('time')
		ydata = data_objects.values_list('value')

	else:
		# Add error message to form

		# Display some data from the MinuteData table

		# Queryset for getting all objects, ordered by time
		data_objects = MinuteData.objects.order_by('time')[:10]

		# Chart stuff -------------------
		xdata = [1, 2, 3, 4, 5] # data_objects.values_list('time')
		ydata = MinuteData.objects.all().values_list('value')


	# Get the objects as a list
	data_list = get_list_or_404(data_objects)

	# Queryset for time intervals
	time_interval_choices = TimeIntervals.time_interval_choices

	chartdata = {'x': xdata, 'y': ydata}
	charttype = "lineChart"
	chartcontainer = 'linechart_container'

	# Map template var name to Python obj
	context = {'data_list': data_list,
				'choices': time_interval_choices,
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

