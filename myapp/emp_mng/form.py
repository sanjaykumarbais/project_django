from django import forms
from .models import Emp_mng

class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=100)
    name=forms.CharField(label="Enter your name",max_length=100)
    feedback=forms.CharField(label="Your feedback",widget=forms.Textarea)

def __init__(self, *args, **kwargs):
    super(FeedbackForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control'


class Emp_mngForm(forms.ModelForm):
    class Meta:
        model=Emp_mng
        fields=['name','emp_id','phone','address']