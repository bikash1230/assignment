from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import DetailsForm 
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Crud(View):
    def get(self,request):
        if request.method == 'GET':
            fm = DetailsForm(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['category']
                im = fm.cleaned_data['image']
                pw = fm.cleaned_data['description']
                reg =Product(name=nm,category=em,image=im,description=pw)
                reg.save()
                fm = DetailsForm()

        else:
            fm = DetailsForm()

        std = Product.objects.all()
        return render(request,'crud.html',{'form':fm,'std':std})

    def post(self,request):
        if request.method == 'POST':
            fm = DetailsForm(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['category']
                im = fm.cleaned_data['image']
                pw = fm.cleaned_data['description']
                reg =Product(name=nm,category=em,image=im,description=pw)
                reg.save()
            return redirect('crud')


    





