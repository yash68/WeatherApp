from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
import requests
from django.contrib import messages

# Create your views here.
def index(request):
	context = {}

	if request.method == 'POST' and 'addcity' in request.POST:
		print("Tere bhakto ki lagi hai katar bhawani")
		cty = City(name = request.POST.get('city'))
		cty.save()

	if request.method == 'POST' and 'tempchange' in request.POST:
		cty = request.POST.get('cityid')
		cty = City.objects.get(cityid = cty)
		if cty.flag == 1:
			cty.flag = 0
		else:
			cty.flag = 1
		cty.save()
		print("Ma Sherwaliye tera sher aa gya")
	
	weather_data = []
	cities = City.objects.all()
	try:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f4af031f6c2086b8dd47171ed8547c3e'
		for city in cities:
			
			try:
				cweather = requests.get(url.format(city)).json()
				cc = City.objects.get(name = city)
				temp = cweather['main']['temp']
				
				cc.ftemp = "{:.1f}".format(temp)
				cc.ctemp = "{:.1f}".format((temp - 32) * 5/9)
				cc.cityid = city.id
				cc.description = cweather['weather'][0]['description']
				cc.icon = cweather['weather'][0]['icon']
				cc.save()

				weather = {
					'city' : city,
					'id' : city.id,
					'description' : cc.description,
					'icon' : cc.icon,
					'flag' : cc.flag,
				}
				
				if cc.flag == 0:
					weather['temprature'] = cc.ctemp
				else:
					weather['temprature'] = cc.ftemp
				
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