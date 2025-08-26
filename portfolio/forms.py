from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    # Honeypot hidden field (should stay empty). Using CharField without required and adding CSS to hide.
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'tabindex': '-1',
        'aria-hidden': 'true',
        'class': 'hp-field'
    }))
    timestamp = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message', 'website', 'timestamp']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['name', 'email', 'subject', 'message']:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean_website(self):
        value = self.cleaned_data.get('website')
        if value:
            # Any value means likely bot
            raise forms.ValidationError('Invalid submission.')
        return value

    def clean_timestamp(self):
        # Basic time-based spam measure (optional placeholder)
        # Could parse epoch ms and ensure not instantaneous, but keeping simple.
        return self.cleaned_data.get('timestamp')
