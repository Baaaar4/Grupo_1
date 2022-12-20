from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
import datetime
import random 
from django.template import Context
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from castillo_barbara.forms import IdeaForm, LoginForm, PensamientoForm
from castillo_barbara.models import Idea, Pensamiento
from django.utils import timezone

# Create your views here.

def home(request):
        # Verificar que no exista la sesión
    if not request.session.has_key('username'):
        # Si la sesión no existe, entonces me lleva al login
        return HttpResponseRedirect('/login')

    username = request.session['username']

    fecha=datetime.datetime.now()
    hora=fecha.hour


    if request.method == 'POST':
        form = PensamientoForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.usuario = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PensamientoForm()


    idea = Pensamiento.objects.all().order_by("-published_date")
 
    
    context = {
        "form": form,
        "username": username,
        "saludos":hora,
        "ideas" : idea
    }

    return render(request, 'home.html', context=context)
    
   

def signin(request):
     # Verificar que no exista la sesión
    if request.session.has_key('username'):
        # Si la sesión existe, entonces me lleva al home
        return HttpResponseRedirect('/')
    else:
        # Si la sesión no existe, verifica el formulario
        if request.method == 'POST':
            # Si se recibe el formulario
            form = LoginForm(request.POST)
            if form.is_valid():
                # Si el formulario es válido, se verifican los datos
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                # Usa la función authenticate de django.contrib.auth
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Si los datos son válidos, crea la sesión
                    request.session['username'] = user.first_name or user.username
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                     return render(request, 'signin.html',{
                    'form': AuthenticationForm,
                    'error': 'El usuario o la contraseña son incorrectas'
        })

            
                    
        else:
            # Si no estamos recibiendo el formulario, entonces envíamos uno vacío
            form = LoginForm()
            #'error': 'El usuario o la contraseña son incorrectas'
            return render(request, 'signin.html', {'form': form })

    return render(request, 'signin.html', {'form': form})


def cerrar(request):
    logout(request)
    return redirect ('signin')
