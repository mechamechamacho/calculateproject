from django import forms
from django.core.exceptions import ValidationError

# Create your models here.

class WarikanForm(forms.Form):
    sum = forms.IntegerField()
    anum = forms.IntegerField()
    bnum = forms.IntegerField()
    cnum = forms.IntegerField()
    diffab = forms.IntegerField()
    diffac = forms.IntegerField()

    def clean(self):
        data = super().clean()
        sum = data['sum']
        anum = data['anum']
        bnum = data['bnum']
        cnum = data['cnum']
        diffab = data['diffab']
        diffac = data['diffac']
        if sum <= 99:
            raise ValidationError("合計金額が間違っています")
        return data
        if sum is None:
            raise ValidationError("合計金額を入力してください")
        return data