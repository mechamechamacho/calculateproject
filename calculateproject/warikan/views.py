from django.shortcuts import render
from django.views.generic import FormView
import math
from django.core.exceptions import ValidationError
from . import forms

# Create your views here.



class Creator(FormView):
    form_class = forms.WarikanForm
    template_name = "create.html"

    def form_valid(self, form):
        data = form.cleaned_data
        sum = data['sum']
        anum = data['anum']
        bnum = data['bnum']
        cnum = data['cnum']
        diffab = data['diffab']
        diffac = data['diffac']


        aprice = ( sum + diffab*bnum + diffac*cnum )/( anum + bnum + cnum )
        bprice = aprice - diffab
        cprice = aprice - diffac
        inta = math.ceil(aprice)
        intb = math.ceil(bprice)
        intc = math.ceil(cprice)
        if cnum == 0:
            intc = 0
        if bnum == 0:
            intb = 0
        
        asum = inta*anum
        bsum = intb*bnum
        csum = intc*cnum
        new_sum = asum + bsum + csum
        remain = new_sum - sum 

        ctxt = self.get_context_data(sum=sum, new_sum=new_sum, remain=remain, anum=anum, bnum=bnum, cnum=cnum, inta=inta, intb=intb, intc=intc, asum=asum, bsum=bsum, csum=csum, form=form)
        return self.render_to_response(ctxt)

        




