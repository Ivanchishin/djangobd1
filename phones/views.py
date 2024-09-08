from django.db.models import Max, Min
from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    try:
        sorting = request.GET.get('sort')
    except:
        sorting = 'name'
    template = 'catalog.html'
    if sorting == 'name':
        phones = Phone.objects.all().order_by(sorting)
    elif sorting == 'max_price':
        phones = Phone.objects.annotate(max_price=Max('price')).order_by('-max_price')
    elif sorting == 'min_price':
        phones = Phone.objects.all().order_by('price')
    context = {'phones': phones,
               'sort_by': sorting}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
