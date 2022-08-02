from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import ProcessorBrand, Processor


class ProcessorBrandList(ListView):
    model = ProcessorBrand
    template_name = 'processor/brand.html'


class PrcessorList(ListView):
    model = Processor
    template_name = 'processor/processor_list.html'