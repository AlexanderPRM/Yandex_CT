from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView): # Выполняет рендеринг заданного шаблона с контекстом, содержащим параметры, захваченные в URL.
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        return context


