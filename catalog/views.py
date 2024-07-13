from django.shortcuts import render

from catalog.models import Product


def index(request):
    product_list = Product.objects.all()
    content = {
        'object_list': product_list,
        "title": "Каталог"
    }
    return render(request, 'catalog/home.html', content)


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name)
        print(phone)
        print(message)
    content = {
        "title": "Контакты"
    }
    return render(request, 'catalog/contacts.html', content)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    content = {
        'object': product,
        "title": product.name
    }
    return render(request, 'catalog/product_detail.html', content)
