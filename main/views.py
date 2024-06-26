from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    context = {
        'title': 'Home - Главное меню',
        'content': 'Магазин настольного тенниса',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Наша компания появилась в 90-х годах, когда в мире настольного тенниса царили другие правила, мы наблюдали за ходом истории в нашем виде спорта, и параллельно успешно развивались. Сегодня наш каталог товаров для настольного тенниса состоит из тысяч единиц разнообразных товаров, и постоянно пополняется. Здесь можно купить накладки, основания, мячи, клеи и средства по уходу за теннисной ракеткой, а также теннисную форму и обувь, различные сопутствующие товары и аксессуары. Мы работаем с самыми известными брендами: Andro, Butterfly, Yasaka, TSP, Victas, Nittaku, Xiom, Joola, Gewo, Friendship, Dr.Neubauer, Tibhar, Donic, DHS, Stiga и многие другие. Если вы уже обращались в наш интернет-магазин, то с легкостью сможете найти интересующий вас товар, используя удобные и понятные фильтры. Также советуем использовать поиск по наименованию товаров, который ускорит процесс вашего выбора."
    }
    return render(request, 'main/about.html', context)