from django.shortcuts import render
from django.http import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request,"frontuser/index.html")

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

