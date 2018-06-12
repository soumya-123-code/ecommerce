from django.urls import path
from frontuser.views import UserCreate, CategoryList,IphoneList,TshirtList


from . import views
app_name="frontuser"

urlpatterns = [
    path('', CategoryList.as_view(), name='home'),
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('registration', views.registration, name="registration"),
    path('shirt', TshirtList.as_view(), name="shirtpack"),
    path('iphone',IphoneList.as_view(),name="iphone"),
]

