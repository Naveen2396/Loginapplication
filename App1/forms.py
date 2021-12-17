from django import forms
from.models import Tasklist # form App1.models import Tasklist

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Tasklist
        fields = ['task','done']
