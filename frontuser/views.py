from django.shortcuts import render
from django.http import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from frontuser.models import Product
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib.auth import authenticate, login
from frontuser.models import Cart, Product
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    men=Product.objects.filter(main_menu='mn')
    return render(request,'frontuser/index.html',{'men':men})



def registration(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        print(data)

        firstname=data.get('fname')
        lastname=data.get('lname')
        email=data.get('email')
        username=data.get('uname')
        password=data.get('p')
        confirmpass=data.get('c')
        if password == confirmpass:
            user=User.objects.create_user(username,email=email,password=password,first_name=firstname,last_name=lastname)
        return HttpResponse("success")




def cartcreate(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        print(data)
        productId=data.get('pdi')
        quantity=data.get('qnt')
        size=data.get('sz')
        my_object = get_object_or_404(Product, pk=productId)
     
        user=Cart.objects.create(profile=request.user,quantity=quantity,product=my_object,size=size)
        return HttpResponse("success")


         



def addproduct(request,product_id):
    my_object = get_object_or_404(Product, pk=product_id)
    product_object = Cart.objects.create(profile=request.user, product=my_object)
    return HttpResponse("success")
    
def addwish(request,product_id):
    my_object = get_object_or_404(Product, pk=product_id)
    product_object = Cart.objects.create(profile=request.user, product=my_object)

def cartdetails(request):
    my_object = Cart.objects.filter(profile=request.user)
    for obj in my_object:
        print(obj.product) 
    return render(request, 'frontuser/cartdetails.html', {'my_object': my_object})

def removecart(request,product_id):
    obj=get_object_or_404(Cart, product=product_id)
    obj.delete()
    return HttpResponse("successfully deleted")

def modalbox(request, product_id):
    my_object = get_object_or_404(Product, pk=product_id)  
    return render(request, 'frontuser/modal.html', {'obj': my_object})


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class UserCreate(AjaxableResponseMixin, CreateView):
    template_name = "frontuser/registration2.html"
    model = User
    fields = ['username','email','first_name','last_name','password']


def mylogin(request):
    if request.method == 'POST' and request.is_ajax():
        data = json.loads(request.body)
        print(data)
        uname=data.get('uname')
        pword=data.get('p')
        user = authenticate(username=uname, password=pword)
        if user is not None:
            if user.is_active:
                login(request,user)
                print("hi")
            else:
                print("fellow")
            data = {"authresponse":"login Successful"}
            return JsonResponse(data)
        else:
            data = {"authresponse":"Username and password invalid"}
            return JsonResponse(data)

def details(request,id):
    try:
        p = Product.object.get(pk=id)
    except Product.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, 'polls/details.html', {"p":p})


