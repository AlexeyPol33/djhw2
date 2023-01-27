from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    return HttpResponse()

def get_recipes(request,recipes):
    servings = 1
    if recipes.lower() not in list(DATA.keys()):
        return HttpResponse('Рецепт не найден')

    if request.GET.get('servings'):
        servings = request.GET.get('servings')
        if servings.isdigit() and int(servings) > 0:
            servings = int(servings)
    
    context = {}
    for ingredient, quantity in DATA[recipes].items():
        context[ingredient] = round (quantity * servings,3)

    context = {'recipe':context}

    return render(request,'calculator/index.html',context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
