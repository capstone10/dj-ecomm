from django.shortcuts import render
from ecommerce.inventory import models


def home(request):
    return render(request, "index.html", {})


def category(request):
    data = models.Category.objects.all()

    print(models.Category.objects.all().query)

    return render(request, "category.html",{"data":data})


def product_by_category(request, category):
    print(category)
    product = models.Product.objects.filter(category__name=category).filter(product__is_default=True).values("id","name","slug","category__name","product__store_price")
    print(product)

    return render(request, "product_by_category.html",{"product":product})
