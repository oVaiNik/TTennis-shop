from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
        if isinstance(goods, list):
            goods = Products.objects.filter(id__in=[item.id for item in goods])
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404("Категория не найдена")

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 9)
    current_page = paginator.page(int(page))
    
    context = {
        "title": "Free style - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product,
    }
    return render(request, "goods/product.html", context=context)