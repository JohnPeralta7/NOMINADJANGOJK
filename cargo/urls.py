from django.urls import path
from .views import cargos, cargos_create, cargos_update, cargos_delete

app_name = 'cargo'

urlpatterns = [
    path('cargos/', cargos, name='cargos'),
    path('crear/', cargos_create, name='cargos_create'),
    path('editar/<int:id>', cargos_update, name='cargos_update'),
    path('eliminar/<int:id>', cargos_delete, name='cargos_delete')
]