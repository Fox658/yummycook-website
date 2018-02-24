from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    paginator= Paginator(articles, 10)
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
    
    template = "articles/article_list.html"
    context = {
        'articles':articles,
        'items':items,
        'page_range':page_range,
    }
    return render(request, template, context)

def article_detail(request,slug):
    article= Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:  
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html',{'form':form})

def buscar(request):
    template = 'articles/article_list.html'

    query = request.GET.get('q')

    results = Article.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-date')

    paginator= Paginator(results, 10)
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
    
    context = {
        'items': results,
        'page_range':page_range,
    }

    return render(request,template,context)