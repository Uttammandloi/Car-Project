from django.shortcuts import render
from .models import team
from cars.models import car

# Create your views here.


def home(request):
    teams = team.objects.all()
    featured_cars = car.objects.order_by(
        '-created_date').filter(is_featured=True)

    all_cars = car.objects.order_by('-created_date')
    #search_fields = car.objects.values('model','city','year','body_style',)
    modle_search = car.objects.values_list('model',flat=True).distinct()
    city_search = car.objects.values_list('city',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    body_style_search = car.objects.values_list('body_style',flat=True).distinct()
    data = {
        "teams": teams,
        "featured_cars": featured_cars,
        "all_cars": all_cars,
        "modle_search":modle_search,
        "city_search":city_search,
        "year_search": year_search,
        "body_style_search":body_style_search,
        
        #"search_fields": search_fields,

    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = team.objects.all()
    data = {
        "teams": teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
