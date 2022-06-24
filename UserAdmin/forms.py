from django import forms
from .models import *
from Freelancing.models import ProjectDetail

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = (
            'title','price','technology','company','start_date','end_date','project_status', 
        )

    def __init__(self, *args, **kargs):
        super(ProjectForm, self).__init__(*args, **kargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['technology'].widget.attrs.update({'class': 'form-control'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'class': 'form-control','type': 'date'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control','type': 'date'})
        self.fields['project_status'].widget.attrs.update({'class': 'form-control'})
       
      


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
    
    def __init__(self, *args, **kargs):
        super(WebsiteForm, self).__init__(*args, **kargs)
        self.fields['website_name'].widget.attrs.update({'class': 'form-control'})
        # self.fields['logo'].widget.attrs.update({'class': 'form-control'})
        # self.fields['favicon'].widget.attrs.update({'class': 'form-control'})

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super(AddressForm, self).__init__(*args, **kargs)
        self.fields['address1'].widget.attrs.update({'class': 'form-control'})
        self.fields['address2'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['zip_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('state')

