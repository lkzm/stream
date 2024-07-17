from django import forms

class UploadSetForm(forms.Form):
    set = forms.FileField()
class UploadVidForm(forms.Form):
    vid = forms.FileField()