from django.urls import path,re_path
from frontuser.views import UserCreate, CategoryList,IphoneList,TshirtList,ShooesList, registration
from . import views


app_name="frontuser"

urlpatterns = [
    path('', CategoryList.as_view(), name='home'),
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('registration', views.registration, name="signup"),
    path('shirt', TshirtList.as_view(), name="shirtpack"),
    path('iphone',IphoneList.as_view(),name="iphone"),
    path('shooes',ShooesList.as_view(),name="shooes"),
    path('login',views.mylogin,name="login"),
    re_path(r'^cart/(?P<product_id>[0-9])/$',views.addproduct,name="addcart"),

    re_path(r'^wish/(?P<product_id>[0-9])/$', views.addwish),
   

]   

