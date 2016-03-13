#coding:utf-8
from django.core.management.base import BaseCommand, CommandError
import pyowm

class Command(BaseCommand):
    help = 'Get weather'

    def add_arguments(self, parser):
        parser.add_argument('city', nargs='+', type=str)


    def handle(self, *args, **kwargs):
        owm = pyowm.OWM('3eeba5f74c7c699dda9d356db366b487')
        city = kwargs['city'][0]
        obj = owm.weather_at_place(city)
        w = obj.get_weather().get_temperature('celsius')
        self.stdout.write(self.style.SUCCESS('Weather in %s - %s'%(city.decode('utf-8'), w.get('temp'))))
        
