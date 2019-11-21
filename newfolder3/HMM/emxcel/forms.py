from django.forms import ModelForm
from emxcel.models import User
# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from django.forms.widgets import passwordInput, TextInput

class Userhome(ModelForm):
    class Meta:
        model=User
        # fields="__all__"
        fields=["username","password","email","contact_no"]

    # def __init__(self,*args,**kwargs):
    #     super(Userhome,self).__init__(*args, **kwargs)
    #     self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholer':'username'})
    #     self.fields['username'].label = False
    #     self.fields['password'].widget = forms.passwordInput(attrs={'class':'form-control', 'placeholer':'password'})
    #     self.fields['password'].label = False
    

# class UploadFileForm(forms.Form):
#     title=forms.CharField(max_length=50)
#     file=forms.FileField()

# class resmodelForm(ModelForm):
#     class Meta:
#         model = resmodel
#         