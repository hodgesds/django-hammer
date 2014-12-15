from django import forms

class DemoForm(forms.Form):
    your_name = forms.FileField(label='SQL File', max_length=100)