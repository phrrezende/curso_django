from django.shortcuts import render
from django.http import HttpResponse

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