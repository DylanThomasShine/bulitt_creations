from django import forms
from .widgets import CustomClearableFileInput
from .models import Commission


class CommissionForm(forms.ModelForm):

    class Meta:
        model = Commission
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
# added 'form-control' for responsiveness

    def __init__(self, *args, **kwargs):
        super(CommissionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

