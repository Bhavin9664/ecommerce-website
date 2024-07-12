from django.urls import path,include

from . import views

app_name = 'store'

urlpatterns = [ 
    path('',views.products_all,name='products_all'),
    path('<slug:slug>',views.product_detail,name="product_detail"),
    path('search/<slug:category_slug>/',views.category_list,name='category_list'),
    path('search/',views.search_list,name='search_list'),
]