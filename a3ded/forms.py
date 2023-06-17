from django import forms
from .models import Grade, Arbi, Francai, Anglai


class TeacherLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-field'}))


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['test']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self.instance, Arbi):
            self.fields['test'].label = 'Test'
        else:
            self.fields['test'].label = 'Test'


class ArbiGradeForm(forms.ModelForm):
    class Meta:
        model = Arbi
        fields = ['test', 'chifehi', 'kira2a', 'intej']


class FrancaiGradeForm(forms.ModelForm):
    class Meta:
        model = Francai
        fields = ['test', 'exp', 'lecture', 'production']


class AnglaiGradeForm(forms.ModelForm):
    class Meta:
        model = Anglai
        fields = ['test', 'oral']
