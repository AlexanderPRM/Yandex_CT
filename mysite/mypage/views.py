from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    '''Создаю представление на основе класса TemplateView'''

    template_name = 'homepage.html' # Файл в котором находится тег-разметка моей страницы.

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context


