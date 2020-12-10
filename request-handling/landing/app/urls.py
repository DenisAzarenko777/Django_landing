from django.urls import path

from app.views import landing, stats, index, tt


urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
    path('tt', tt, name = 'test')
]
