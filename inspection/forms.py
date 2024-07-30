from django.forms import ModelForm
from .models import CCOS

class CCOSCreationForm(ModelForm):
    class Meta:
        model = CCOS
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['project'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['discipline'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['yard'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['owner'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['_class'].widget.attrs.update({'class': 'searchable-select'})