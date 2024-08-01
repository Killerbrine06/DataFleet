
from django.urls import path
from project.views import element_view

urlpatterns = [
    path('elements/<int:id>', element_view, name='element_page')
]
