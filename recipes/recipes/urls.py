from django.urls import path
# from django.contrib import admin
from calculator.views import dish
# from other_app.views import Home
# from my_app import views
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
urlpatterns = [path(dish1+'/', dish) for dish1 in DATA]

    # path('omlet/', dish(DATA),
    # здесь зарегистрируйте вашу view-функцию

