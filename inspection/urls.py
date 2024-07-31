from django.urls import path
from .views import *

urlpatterns = [
    path('add/', new_ccos_view, name='new_ccos_page'),
    path('<int:id>', ccos_view, name='ccos_page'),
    path('', ccos_list_view, name='ccos_list_page'),
]
