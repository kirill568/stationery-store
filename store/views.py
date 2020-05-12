from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.db.models import Q

from store.models import *

itemOnThePage = 6

def isAuth(request):
    if not request.user.is_authenticated and not request.user.is_staff:
        return False
    return True

def pagination(products, itemPage, pageNumber):
	paginator = Paginator(products, itemOnThePage)
	page = paginator.get_page(pageNumber)
	isPaginated = page.has_other_pages()

	if page.has_previous():
		prevUrl = '?page={}'.format(page.previous_page_number())
	else:
		prevUrl = ''

	if page.has_next():
		nextUrl = '?page={}'.format(page.next_page_number())
	else:
		nextUrl = ''

	return {'nextUrl': nextUrl, 'prevUrl': prevUrl, 'page': page, 'isPaginated': isPaginated}

def productList(request, products=None, categoryName=''):

	if products is None:
		products = Product.objects.all()

	categories = Category.objects.filter(parent__isnull=True) #categories which don't have parent

	pageNumber = request.GET.get('page', 1)
	contextPages = pagination(products, itemOnThePage, pageNumber)

	return render(request, 'store/products_list.html', {'categories_list': categories,
														'category_name': categoryName,
														'nextUrl': contextPages['nextUrl'], 
														'prevUrl': contextPages['prevUrl'],
														'page_object': contextPages['page'], 
														'isPaginated': contextPages['isPaginated']})

def productCategory(request, slug):
	category = Category.objects.get(url__iexact = slug)
	categoryName = category.name
	products = category.product_set.all()
	return productList(request, products=products, categoryName=categoryName)

def productSearch(request):
	searchQuery = request.GET.get('search', '')
	products = Product.objects.filter(Q(name__icontains=searchQuery) | Q(description__icontains=searchQuery))
	return productList(request, products=products)

def productDetail(request, slug):
	product = Product.objects.get(url__iexact = slug)
	return render(request, 'store/product_detail.html', {'product': product})

def productSetCount(request, slug):
    count = request.POST.get('count');
    product = Product.objects.get(url__iexact = slug)
    if isAuth(request):
        product.count = count;
        product.save();
        return redirect('productListUrl')
    else:
        return HttpResponse('<h1>ERROR 403</h1>')