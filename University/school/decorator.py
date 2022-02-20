from django.http import HttpResponse
from django.shortcuts import redirect ,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def userauthenticate(view_func):
	def wrapper_func(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('/')

		else: 
			return view_func(request,*args,**kwargs)

	return wrapper_func

def admin_only(view_func):
	def fixer(request,*args,**kwargs):
		group = None
		if  request.user.groups.exists():
			group = request.user.groups.all()[0].name
			print(group)
			print('successfull',group)
		else:
			return redirect('/user')


		if group =='Student':
			return redirect('/user')

		if group == 'Admin':
			return view_func(request,*args,**kwargs)



	return fixer