from django import forms
from .widgets import CustomClearableFileInput
from .models import Commission


class CommissionForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Please give a description of what you would like created and then upload your image below'}))

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
# added 'form-control' for responsiveness

    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Commission
        fields = ('first_name', 'last_name', 'email', 'message', 'image')
