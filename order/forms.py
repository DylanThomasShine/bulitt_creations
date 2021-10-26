from django import forms

from .models import Order
from .widgets import CustomClearableFileInput

class OrderForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    image_url = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Description'}))
    

# added 'form-control' for responsiveness
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = ('name', 'image_url','description', 'image')
