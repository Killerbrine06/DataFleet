from django import forms
from .models import CCOS, Remark

class CCOSCreationForm(forms.ModelForm):
    class Meta:
        model = CCOS
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['project'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['discipline'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['yard'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['owner'].widget.attrs.update({'class': 'searchable-select'})
        self.fields['u_class'].widget.attrs.update({'class': 'searchable-select'})
        
class RemarkAdminForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5, 'columns': 80})
        }