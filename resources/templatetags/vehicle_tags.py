from django import template
from datetime import date
from resources.models import Vehicle

register = template.Library()

@register.simple_tag
def get_vehicles(total_items):
    date_vehicle= date(2007,1,1)
    v1 = Vehicle(
    	name="uno",
		license_plate="GOF435",
		manufecture_year=date_vehicle,
		is_active=False
    	)
    v1.save()
    list_vehicle = list()
    list_vehicle.append(v1)
    
  
    return list_vehicle[:total_items]
