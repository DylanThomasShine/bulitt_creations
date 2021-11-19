from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First name'}))  # noqa
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last name'}))  # noqa
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email address'}))  # noqa
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Message'}))  # noqa

# added 'form-control' for responsiveness

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
