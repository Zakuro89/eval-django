from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import T_Event, T_Participation
from django.db.models import Count
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def login(request):
  error = None

  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      
      user = authenticate(request, username=username, password=password)

      if user:
            auth_login(request, user)
            return redirect('events-list')
      else:
            error = "❌ Nom d'utilisateur ou mot de passe incorrect !"

  return render(request, 'login.html', {'error': error})

def events_list(request):
  events = T_Event.objects.annotate(nb_participants=Count('participations'))
   
  return render(request, 'events-list.html', {'events': events, 'user': request.user})
  
@login_required
def event_details(request, event_id):
   
  event = get_object_or_404(T_Event, id=event_id)
  event.nb_participants = event.participations.count()

  if request.method == 'POST' and request.user.is_authenticated:
    T_Participation.objects.get_or_create(user_id=request.user, event_id=event)
  
  return render(request, 'event-details.html', {
    'event': event,
    'user': request.user
  })

       
