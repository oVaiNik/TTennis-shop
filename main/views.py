from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories, Products
from django.utils.safestring import mark_safe
import random


def index(request, all_products = None):
    all_products = list(Products.objects.all())

    random.shuffle(all_products)
    random_products = all_products[:9]
    context = {
        'title': 'Free style - Главное меню',
        'content': 'Магазин мужской одежды и аксессуаров',
        'products': random_products,
    }
    return render(request, 'main/index.html', context)




def about(request):
    context = {
        'title': 'Free style - О нас',
        'content': mark_safe('О нас'),
        'text_on_page': mark_safe(
            "Free style – это магазин модной одежды, где каждый найдет что-то по душе. " \
            "Мы предлагаем стильные, удобные и качественные вещи, которые помогут вам выразить свою индивидуальность.<br><br>" \
            "<strong>Почему выбирают нас?</strong>" \
            "<ul>" \
            "<li><strong>Актуальные тренды </strong>– следим за модными тенденциями и предлагаем только лучшее.</li>" \
            "<li><strong>Качество и комфорт </strong>– работаем с проверенными поставщиками, чтобы вы получали долговечные и приятные к носке вещи.</li>" \
            "<li><strong>Доступные цены </strong>– мода должна быть для всех, поэтому у нас есть варианты на любой бюджет.</li>" \
            "</ul><br>" \
        )
    }
    return render(request, 'main/about.html', context)