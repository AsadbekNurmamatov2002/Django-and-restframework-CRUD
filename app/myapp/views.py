from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def Home(request):
    product=Product.objects.all()
    return render(request, 'index.html', {'product':product})

def CreateView(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "create.html",{'form':form})