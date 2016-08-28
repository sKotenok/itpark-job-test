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
class Category(models.Model):
    name = models.CharField("Группа товара", max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Группа")
    name = models.CharField("Название товара", max_length=128)
    price = models.DecimalField("Стоимость единицы, руб.", max_digits=10, decimal_places=2)


# Views:

def test():
    # 1.
    p1 = Product.objects.filter(price__gte=100) \
        .group_by('-category') \
        .annotate(p_count=Count())

    for product in p1:
        print(product)

    # 2.
    p2 = p1.filter(p_count__gt=10)

    for product in p2:
        print(product)

    #3. Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
    #Название категории товараю
    #наименование товара.
    #Цена.
    p3 = Product.objects.all().values('category__name', 'name', 'price')

    for product in p3:
        print(product)


