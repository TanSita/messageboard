from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def show_messages(request):
	if request.method == 'POST':
		myusername = ""
		mycontent = ""

		try:
			delete_id = request.POST.get('del')
			mess.objects.get(pk=delete_id).delete()
		except:
			print("can't delete .....")

		try:
			myusername = request.POST.get('username')
			mycontent = request.POST.get('mes')
			if(len(myusername)==0):
				myusername = "Human :D"
			if(len(mycontent)==0):
				mycontent = "I'm contents..."
			mess(username=myusername,content=mycontent).save()
		except:
			print("can't insert .....")


	messages = mess.objects.all()

	data = {
		'messages': messages
	}
	return render(request, 'home.html', data)

