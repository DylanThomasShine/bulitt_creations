from django import forms

from .models import Order
from .widgets import CustomClearableFileInput

class OrderForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Please tell us what you would like us to create for you, then simply upload an image for a reference. '}))
    

# added 'form-control' for responsiveness
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = ('name', 'email','description', 'image')
