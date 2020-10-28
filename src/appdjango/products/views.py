from django.shortcuts import render

from .forms import ProductForm #PASO 6

#PASO 4
from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price
    # }

    #PASO5
    context = {
        'object': obj
    }
    return render(request, "product/detail.html", context)

#PASO 6
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "product/create.html", context)

#PASO 7
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/list.html", context)

def product_details_view(request, id):
    obj = Product.objects.get(id=id)

    context = {
        'object': obj
    }
    return render(request, "product/update.html", context)
