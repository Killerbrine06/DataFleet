from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .forms import CCOSCreationForm

def new_ccos_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    
    return render(request, 'new_ccos.html', {'form': CCOSCreationForm()})