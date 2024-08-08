from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from inspection.models import Remark
from .models import Project, Element

def element_view(request, id:int):
    element = get_object_or_404(Element, id=id)
    remarks = Remark.objects.filter(element=element)
    
    return render(request, 'element.html', {'element': element, 'remarks':remarks})