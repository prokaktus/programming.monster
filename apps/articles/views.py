from django.shortcuts import render
from django.views.generic import TemplateView

from apps.articles.models import InfoPage


class HomeView(TemplateView):
    template_name = 'articles/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AboutView(TemplateView):
    template_name = 'articles/about.html'

    def get(self, request, *args, **kwargs):
        page = InfoPage.objects.get(slug='about')
        context = {'page': page}
        return render(request, self.template_name, context)
