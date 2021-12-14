from django.shortcuts import render
from ecommerce.inventory import models


def home(request):
    return render(request, "index.html", {})


def category(request):
    data = models.Category.objects.all()

    print(models.Category.objects.all().query)

    return render(request, "category.html",{"data":data})


def product_by_category(request, category):

    product = models.Product.objects.filter(category__name=category)
    print(product)

    return render(request, "product_by_category.html",{"product":product})
