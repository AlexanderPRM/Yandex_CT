from django.urls import path
from .views import HomePage

# Указываем Django как по адресу запроса найти наш скрипт, т.е определяем URL для представления.
urlpatterns = [
    path('', HomePage.as_view()),
]
