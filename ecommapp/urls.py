from django.urls import path
from ecommapp import views

urlpatterns = [
   
    path('',views.home),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('addition/<x>/<y>',views.addition),
    path('productlist',views.product_list),
    path('base',views.reuse),
    path('register.html',views.register),
    path('sort/<sv>',views.sort),
    path('catfilter/<catv>',views.catfilter),
    path('pricefilter/<pv>',views.pricefilter),
    path('pricerange',views.pricerange),
    path('pdetails/<pid>',views.product_details),
    path('addproduct',views.addproduct),
    path('delproduct/<rid>',views.delproduct),
    path('editproduct/<rid>',views.editproduct),
    path('djangoform',views.djangoform),
    path('modelform',views.modelform),
    path('register',views.user_register),
    path('login',views.user_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('cart/<pid>',views.addtocart),
    path('logout',views.user_logout),
    path('viewcart',views.viewcart),
    path('changeqty/<pid>/<f>',views.changeqty),
    path('placeorder',views.placeorder),
    path('payment',views.makepayment),
    path('store',views.storedetails),
]
