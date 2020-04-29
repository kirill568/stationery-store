from django.urls import path
from .views import *

urlpatterns = [
	path('', productList, name='productListUrl'),
	path('product/search/', productSearch, name='productSearchUrl'),
	path('product/<str:slug>/', productDetail, name='productDetailUrl'),
	path('product/category/<str:slug>/', productCategory, name='productCategoryUrl')
]