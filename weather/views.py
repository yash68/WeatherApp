from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
import requests
from django.contrib import messages

# Create your views here.
def index(request):
	#form  = CityForm()
	context = {}
	if request.method == 'POST':
		cty = City(name = request.POST.get('city'))
		#form  = CityForm(request.POST)
		#if form.is_valid():
		#	form.save()
		cty.save()
	weather_data = []
	cities = City.objects.all()
	try:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f4af031f6c2086b8dd47171ed8547c3e'
		for city in cities:
			try:
				cweather = requests.get(url.format(city)).json()
				temp = cweather['main']['temp']
				temp = (temp - 32) * 5/9
				weather = {
					'city' : city,
					'id' : city.id,
					'temprature' : "{:.1f}".format(temp),
					'description' : cweather['weather'][0]['description'],
					'icon' : cweather['weather'][0]['icon']
				}
				weather_data.append(weather)
			except:
				messages.warning(request, "Error in City name")

	except:
		messages.info(request, "something happen")
	context = {'city_weather' : weather_data}
	return render(request,'index.html', context)

def remove(request, item_id): 
    item = City.objects.get(id=item_id) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return redirect('index') 