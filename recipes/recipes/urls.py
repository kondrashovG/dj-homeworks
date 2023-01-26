from django.urls import path
from calculator.views import dish
from django.conf import settings

urlpatterns = [path(dish1+'/', dish) for dish1 in settings.DATA]

    # здесь зарегистрируйте вашу view-функцию

