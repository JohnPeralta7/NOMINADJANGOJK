from django.urls import path
from .views import cargos

app_name = 'cargo'

urlpatterns = [
    path('cargos/', cargos, name='cargos')
    

]