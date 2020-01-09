from django import forms
from .models import Job


class DateInput(forms.DateInput):
    input_type = 'date'


class TextInput(forms.TextInput):
    input_type = 'text'


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = (
            'title', 'text', 'contact', 'company', 'location', 'postcode',
            'job_type', 'seniority_level', 'last_application_date',
            'apply_link'
        )
        widgets = {
            'contact': TextInput(
                attrs={
                    'placeholder':
                    'example@company.com -it will not appear publically'
                }
            ),
            'postcode': TextInput(attrs={'placeholder': '4 digit postcode'}),
            'last_application_date': DateInput(),
        }
