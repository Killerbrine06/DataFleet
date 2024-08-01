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
    elements = Element.objects.filter(project=inspection.project)

    return render(request, 'ccos_page.html', {'inspection': inspection, 'elements': elements})