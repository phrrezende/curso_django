from django import template

register = template.Library()

@register.simple_tag
def get_vehicles(total_items):
    list_vehicle = list()
    list_vehicle.append('uno')
    list_vehicle.append('gol')
    list_vehicle.append('fox')
    list_vehicle.append('hb20')

    return list_vehicle[:total_items]
