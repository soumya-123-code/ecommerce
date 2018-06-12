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

# Create your views here.
class CategoryList(ListView):
    template_name = 'frontuser/index.html'
    model = Category

class IphoneList(ListView):
    template_name = 'frontuser/iph.html'
    model = Product

class TshirtList(ListView):
    template_name = 'frontuser/shirtflex.html'
    context_object_name = 'shirt_list'
    queryset = Product.objects.filter(category__main_menu="mt")


def registration(request):
	if request.method =='POST':
		form1 = userform(request.POST)
		if form.is_valid():
			username = form1.cleaned_data['username']
			first_name = form1.cleaned_data['first_name']
			last_name = form1.cleaned_data['last_name']
			email = form1.cleaned_data['email']
			password = form1.cleaned_data['password']
			User.objects.create_user(username = username,first_name=first_name,last_name=last_name,email=email,password=password)
			return HttpResponseRedirect('/registration')

	else:
		form1=userform()
	return render(request,'frontuser/registration.html',{'frm':form1})




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


