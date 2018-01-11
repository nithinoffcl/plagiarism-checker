from django import forms
from .models import Data,Document

class DataForm(forms.ModelForm):
	# post = forms.CharField(max_length=280)

	class Meta:
		model = Data
		fields = ('data',)

class Documents(forms.ModelForm):

	class Meta:
		model = Document
		fields = ('document','description',)

#class UploadFileForm(forms.Form):
#    title = forms.CharField(max_length=50)
    #file = forms.FileField()
