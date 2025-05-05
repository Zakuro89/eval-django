from django.contrib import admin
from eventManagerApp.models import T_Event, T_Participation


admin.site.register([T_Event, T_Participation])