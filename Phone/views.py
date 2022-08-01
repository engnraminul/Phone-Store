from django.shortcuts import render

from django.views.generic import ListView
from .models import ProcessorBrand


class ProcessorBrandList(ListView):
    model = ProcessorBrand
    template_name = 'processor/brand.html'
