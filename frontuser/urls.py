from django.urls import path,re_path
from frontuser.views import UserCreate,registration
from . import views


app_name="frontuser"

urlpatterns = [
    path('',views.home,name='home'),
    path('cartcreate',views.cartcreate,name='cartcreate'),
    
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('registration', views.registration, name="signup"),
   
    path('login',views.mylogin,name="login"),
    re_path(r'^cart/(?P<product_id>[0-9])/$',views.addproduct,name="addcart"),

    re_path(r'^wish/(?P<product_id>[0-9])/$', views.addwish),
    path('cartdetails', views.cartdetails, name="cartdetails"),
    re_path(r'removecart/(?P<product_id>[0-9])/$', views.removecart, name="removecart"),
    re_path(r'modalbox/(?P<product_id>[0-9])/$', views.modalbox, name="modalbox")
   

]   