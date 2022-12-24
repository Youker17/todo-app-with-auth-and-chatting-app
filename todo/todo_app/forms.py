from django import forms



class AddTaskForm(forms.Form):
    name = forms.CharField(required=True)
    date = forms.DateField(required=True)
