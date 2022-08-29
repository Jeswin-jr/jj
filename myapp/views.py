from  django.shortcuts import render,redirect
from.forms import customerform
from .models import customer
from django.views.generic.base import  TemplateView
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
def home(request):
    object=customer.objects.all()
    return render(request,'home.html',{'data':object})
def create(request):
    if request.method=="POST":
        form=customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('create')
    else:
       form=customerform
       return render(request,'create.html',{'form':form})
def update(request,id):
    obj=customer.objects.get(id=id)
    if request.method=="POST":
        form=customerform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('read')
        return redirect('create')
    else:
        form=customerform
        return render(request,'update.html',{'form':form})
def delete(request,id):

    obj=customer.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        return redirect('read')
    return render(request,'delete.html')

class payment(TemplateView):
    template_name = 'payment.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['key']=settings.STRIPE_PUBLISHABLE_KEY
        return context
def charge(request):
    if request.method=='POST':
        def charge(request):
            if request.method=="POST":
                charge=stripe.Charge.create(amount=900,
                                            currency='inr',
                                            description='payment',
                                            source=request.POST['stripeToken']
                )
            return  render(request,'charge.html')
def charge(request):

    return render(request,'charge.html')
