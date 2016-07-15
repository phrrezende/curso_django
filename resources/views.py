from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from datetime import date



# Create your views here.

def index(request):

    context_return= {
    'course_name' : 'Python e Django',
     'alunos_list': [
         {
         'name' : 'Sebastião'
         },
         {
         'name' : 'Daniela'
         },
         {
         'name' : 'Paulo'
         }
     ]
    }
    return render(request, "hello.html", context_return)
    # return HttpResponse("Olá! Você realizou sua primeira requisição!")

def usecontrol_add(request):
    date_vehicle= date(2007,1,1)
    driver = Driver(name="Paulo")
    driver.save()

    manufacturer= Manufacture(name="Fiat")
    manufacturer.save()

    vehicle= Vehicle(name="Uno", license_plate="GOF343",manufacture_year=date_vehicle, manufaturer=manufacturer, description="Carro Bão")
    vehicle.save()

    use_control= UseControl(
        driver=driver,
        vehicle=vehicle
        )
    use_control.save()

    return HttpResponse("Dados Salvos com Sucesso")


def usecontrol_list(request):
    usecontrol= UseControl.objects.all().first()
    data={
        'vehicle': usecontrol.vehicle.name,
        'driver':  usecontrol.driver.name,
        'date_started': usecontrol.date_started
    }
    return HttpResponse(request, 'use_control_list.html', data)

class UseControlView(TemplateView):
    template_name = "usecontrol_list.html"

    def get_context_data(self, **kwargs):
        context= super(UseControlView, self).get_context_data(**kwargs)
        context['avaible_vehicles'] = Vehicle.objects.all()[:5]
        return context


class VehicleCreate(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields= ['name','description','license_plate', 'manufaturer','manufacture_year']

class VehicleUpdate(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields= ['name','description','license_plate','manufaturer', 'manufacture_year']


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url= reverse_lazy('vehicle_list')
    template_name= 'vehicle_confirm_delete.html'

class VehicleList(ListView):
    model= Vehicle
    template_name= 'list_vehicle.html'
    queryset= Vehicle.objects.order_by('name')
    context_object_name= 'vehicle_list'
