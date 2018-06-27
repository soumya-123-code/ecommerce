from django.shortcuts import render
from django.http import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from frontuser.models import Product, Category
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib.auth import authenticate, login
from frontuser.models import Cart, Product
from django.shortcuts import get_object_or_404

# Create your views here.
class CategoryList(ListView):
    template_name = 'frontuser/index.html'
    model = Category

class IphoneList(ListView):
    template_name = 'frontuser/iph.html'
    context_object_name="iphone_list"
    queryset=Product.objects.filter(category__main_menu="mb")

class TshirtList(ListView):
    template_name = 'frontuser/shirtflex.html'
    context_object_name = 'shirt_list'
    queryset = Product.objects.filter(category__main_menu="mt")

class ShooesList(ListView):
    template_name = 'frontuser/nike.html'
    context_object_name = 'shooes_list'
    queryset = Product.objects.filter(category__main_menu="sh")


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

def addproduct(request,product_id):
    my_object = get_object_or_404(Product, pk=product_id)
    product_object = Cart.objects.create(profile=request.user, product=my_object)
    return HttpResponse("success")
    
def addwish(request,product_id):
    my_object = get_object_or_404(Product, pk=product_id)
    product_object = Cart.objects.create(profile=request.user, product=my_object)



         
   



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











#Views.py extract





def test_view(request):
    # Based on the user who is making the request, grab the cart object
    my_cart = Cart.objects.get_or_create(user=User)
    # Get entries in the cart
    my_carts_current_entries = Entry.objects.filter(cart=my_cart)
    # Get a list of your products
    products = Product.objects.all()

    if request.POST:
        # Get the product's ID from the POST request.
        product_id = request.POST.get('product_id')
        # Get the object using our unique primary key
        product_obj = Product.objects.get(id=product_id)
        # Get the quantity of the product desired.
        product_quantity = request.POST.get('product_quantity')
        # Create the new Entry...this will update the cart on creation
        Entry.objects.create(cart=my_cart, product=product_obj, quantity=product_quantity)
        return HttpResponse('somewhereelse.html')

    return render(request, 'something.html', {'my_cart': my_cart, 'my_carts_current_entries': my_carts_current_entries,
                                              'products': products})