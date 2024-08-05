from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied

from project.models import Element
from .forms import CCOSCreationForm
from .models import CCOS

def new_ccos_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = CCOSCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('index_page')
        
        return render(request, 'new_ccos.html', {'form': form})
    
    form = CCOSCreationForm()
    
    return render(request, 'new_ccos.html', {'form': form})

def ccos_list_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    inspections = CCOS.objects.all()
    
    return render(request, 'ccos_list.html', {'inspections': inspections})

def ccos_view(request, id:int):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    inspection = get_object_or_404(CCOS, id=id)
    added_elements = Element.objects.filter(inspection=inspection)
    available_elements = Element.objects.filter(project=inspection.project)
    available_unused_elements = []
    
    x = 0
    y = 0
    
    while x < len(added_elements) and y < len(available_elements):
        if added_elements[x].id < available_elements[y].id:
            x += 1
        
        elif added_elements[x].id == available_elements[y].id:
            x += 1
            y += 1
            
        else: 
            available_unused_elements.append(available_elements[y])
            y += 1
            
    
    while y < len(available_elements):
        available_unused_elements.append(available_elements[y])
        y += 1
        
    return render(request, 'ccos_page.html', {'inspection': inspection, 'added_elements': added_elements, 'available_elements': available_unused_elements})

def add_element_view(request, id:int, element_id:int):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    inspection = get_object_or_404(CCOS, id=id)
    element = get_object_or_404(Element, id=element_id)
    
    if not (element.inspection or element.discipline != inspection.discipline or element.project != inspection.project):
        element.inspection = inspection
        element.save()
    
    return redirect(f'/ccos/{id}')
