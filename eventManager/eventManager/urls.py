"""
URL configuration for eventManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventManagerApp.views import events_list, login, event_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events_list, name='index'),
    path('events-list/', events_list, name="events-list"),
    path('login/', login, name="login"),
    path('events/<int:event_id>/', event_details, name='event-details')
]
