import json

from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

from products.models import Menu, Category, Product

# Create your views here.

class ProductsView(View):
    def post(self, request):
        data = json.loads(request.body)
        menu = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
        )
        Product.objects.create(
            name = data['product'],
            menu = menu,
            category = category
        )
        return JsonResponse({'MESSAGE': 'CREATED'}, status = 201)