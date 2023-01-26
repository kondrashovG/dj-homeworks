from django.shortcuts import render
from django.conf import settings


# Напишите ваш обработчик. Используйте DATA как источник данных
# DATA перенесена в settings.py
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def dish(request):
    quantity = {}
    name_dish = request.get_full_path().split('/')[1]
    servings = request.GET.get('servings')
    if not servings:
        servings = 1
    else:
        servings = int(servings)
    for ingredients in settings.DATA[name_dish]:
        quantity[ingredients] = round(settings.DATA[name_dish][ingredients] * servings, 2)
    context = {
        'recipe': {name_dish: quantity}
    }
    print(type(request))
    return render(request, 'calculator/index.html', context)