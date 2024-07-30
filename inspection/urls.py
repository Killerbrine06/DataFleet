from django.urls import path
from .views import new_ccos_view

urlpatterns = [
    path('add/', new_ccos_view, name='new_ccos_page')
]
