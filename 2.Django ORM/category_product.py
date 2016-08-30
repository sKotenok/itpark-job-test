#!/usr/bin/env python3

"""
1. С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб., сгруппировать по категориям и посчитать количество товаров в каждой категории.
2. То же самое, но оставить лишь категории, в которых строго больше 10 товаров.
3. Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
    Название категории товараю
    наименование товара.
    Цена.

По возможности, минимизировать количество обращений к базе данных и количество передаваемых данных.
"""

# Models:
from django.db import models

class Category(models.Model):
    name = models.CharField("Группа товара", max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Группа")
    name = models.CharField("Название товара", max_length=128)
    price = models.DecimalField("Стоимость единицы, руб.", max_digits=10, decimal_places=2)


# Views:

def test(request):
    # 1.
    ## выбрать товары, цена которых больше или равна 100 руб.
    ps = Product.objects.filter(price__gte=100)
    for p in ps:
        print(p.id, p.name, p.price)

    ## сгруппировать по категориям и посчитать количество товаров в каждой категории.
    cs = Category.objects.filter(product__price__gte=100).annotate(p_count=Count('product'))
    for c in cs:
        print(c.name, c.p_count)

    c_by_ids = {c.id: c for c in cs}
    p_by_category = {}
    for p in ps:
        if p.category_id in c_by_ids:
            if not p_by_category[c_by_ids[p.category_id]]:
                p_by_category[c_by_ids[p.category_id]] = []
            p_by_category[c_by_ids[p.category_id]].append(p)
    for c_id, c in c_by_ids.items():
        print(c.name, c.p_count, [(p.name, p.price) for p in p_by_category[c_id]])

    ## Дополнение:
    ## Кто-то на тостере год назад задал вопрос 1 в 1, как в задании, поэтому просто
    ## копирую ответ оттуда.
    categories = Category.objects.filter(product__price__gte=100) \
        .prefetch_related(
            Prefetch('product_set', queryset=Product.objects.filter(price__gte=100))
        ).distinct('id')
    for category in сategories:
        products = category.product_set.all()
        print(category.name, len(products), products)

    ## Внутри происходит примерно то же самое, что и в моей версии
    ## (т.к. prefetch_related делает join средствами питона)


    # 2. оставить лишь категории, в которых строго больше 10 товаров.
    cs = cs.filter(p_count__gt=10)


    #3. Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
    #Название категории товараю
    #наименование товара.
    #Цена.
    ps3 = Product.objects.all().values('category__name', 'name', 'price')

    for product in ps3:
        print(product)

    ## Если нужен не просто пример вывода, а полноценная команда для консоли, добавил
    ## в my_app. Вызывать:
    ## python3 manage.py showproducts
