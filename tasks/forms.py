from django import forms

class TaskForm(forms.Form):
    description = forms.CharField(label='Task', max_length=255)
