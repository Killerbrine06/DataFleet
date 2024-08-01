from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Project, Element

def element_view(request, id:int):
    element = get_object_or_404(Element, id=id)
    
    return render(request, 'element.html', {'element': element})