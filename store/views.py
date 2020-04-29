from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.db.models import Q

from store.models import *

itemOnThePage = 6

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

def productList(request, productSearch=None, productCategory=None, categoryName=''):
	pageNumber = request.GET.get('page', 1)

	if productSearch is not None:
		products = productSearch
	elif productCategory is not None:
		products = productCategory
	else:
		products = Product.objects.all()

	categories = Category.objects.filter(parent__isnull=True) #categories which don't have parent

	contextPages = pagination(products, itemOnThePage, pageNumber)
	print(contextPages)

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
	return productList(request, productCategory=products, categoryName=categoryName)

def productSearch(request):
	searchQuery = request.GET.get('search', '')
	products = Product.objects.filter(Q(name__icontains=searchQuery) | Q(description__icontains=searchQuery))
	return productList(request, productSearch=products)

def productDetail(request, slug):
	product = Product.objects.get(url__iexact = slug)
	return render(request, 'store/product_detail.html', {'product': product})