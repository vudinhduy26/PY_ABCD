from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from django.views import View

class contact(View):
	def get(self,request):
		cc = {'cf123':contact_Form}
		return render(request,'contact/contact.html',cc)
	def post(self,request):
		if request.method == "POST":
			cf123 = contact_Form(request.POST)
			if cf123.is_valid():
				cf123.save()
				return render(request,'contact/contact.html',cc)
		else:
			return HttpResponse("no POST")