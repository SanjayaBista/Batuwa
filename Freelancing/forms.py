from django import forms
from .models import Project, ProjectDetail
from .widgets import DatePickerInput


# class DateInput(forms.DateInput):
#     input_type = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class PostProjectForm(forms.ModelForm):
    period = forms.CharField()

    class Meta:
        model = ProjectDetail
        fields = (
            'title','project','priceType','period',
            'startDate','document','links','description',
        )
        # widgets = {
        #             'startDate' : DateInput(),
                    
        #         }
    def save(self, *args, **kwargs):

        super().save(commit=False)

        start_type  = self.cleaned_data.pop('period','')
        print('\n'*10,start_type)
        if start_type == 'immediate':
            self.cleaned_data['is_start_immediately'] = True
        
        
        pd = ProjectDetail.objects.create(**self.cleaned_data)
        self.save_m2m()
        # super().save(*args, **kwargs)

    def __init__(self, *args, **kargs):
        super(PostProjectForm, self).__init__(*args, **kargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['project'].widget.attrs.update({'class': 'form-control'})
        # self.fields['expertise'].widget.attrs.update({'class': 'form-control'})
        self.fields['priceType'].widget.attrs.update({'class': 'form-control'})
        self.fields['startDate'].widget.attrs.update({'class': 'form-control','type': 'date'})
        self.fields['document'].widget.attrs.update({'class': 'form-control'})
        self.fields['links'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
      
        