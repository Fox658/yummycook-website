from django.shortcuts import render, get_object_or_404
#from django.views.generic import ListView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import SerieTutoriales, Leccion

def serie_tutoriales_list(request):
    tutoriales = SerieTutoriales.objects.all().prefetch_related(
        'tutoriales'
        ).annotate(
            leccion=Count('tutoriales')
        )
    paginator= Paginator(tutoriales, 10)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]

    template= "tutoriales/serietutoriales_list.html"
    context = {
        'tutoriales':tutoriales,
        'items': items,
        'page_range': page_range,
    }
    return render(request, template, context)

def detalle_tutorial_series(request,slug):
    series =  get_object_or_404(SerieTutoriales, slug=slug)
    lecciones = series.tutoriales.filter(serie_tutoriales=series)
    
    template = "tutoriales/detalletutorial_series.html"
    context ={
        'series': series,
        'lecciones':lecciones,
    }
    return render(request,template,context)

def detalle_leccion(request, serie_tutoriales, slug):
    leccion = get_object_or_404(Leccion.objects.filter(
        serie_tutoriales__slug=serie_tutoriales, slug=slug))

    template = "tutoriales/leccion_detail.html"

    context = {
        'leccion': leccion,
    }
    return render(request,template,context)