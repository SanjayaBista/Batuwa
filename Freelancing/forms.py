from django import forms
from .models import Project, ProjectDetail

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = (
            'title','project','expertise','priceType',
            'startDate','document','links','description'
        )
    def clean(self):
        cleaned_data = super(PostProjectForm, self).clean()
    
    def __init__(self, *args, **kargs):
        super(PostProjectForm, self).__init__(*args, **kargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['project'].widget.attrs.update({'class': 'form-control'})
        self.fields['expertise'].widget.attrs.update({'class': 'form-control'})
        self.fields['priceType'].widget.attrs.update({'class': 'form-control'})
        self.fields['startDate'].widget.attrs.update({'class': 'form-control','type': 'date'})
        self.fields['document'].widget.attrs.update({'class': 'form-control'})
        self.fields['links'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
      
        