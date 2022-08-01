from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import ProcessorBrand


class ProcessorBrandList(ListView):
    model = ProcessorBrand
    template_name = 'processor/brand.html'


class PrcessorDetail(DetailView):
    model = ProcessorBrand
    template_name = 'processor/details.html'