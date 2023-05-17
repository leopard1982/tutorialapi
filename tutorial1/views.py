from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def hello_world(request):
	return render(request,'hello_world.html')

def tampilUser(request):
	myreq = requests.get("http://192.168.1.50:8787/api/1/")

	try:
		return render(request,'tampilUser.html',{'data':myreq.json()})
	except:
		return render(request,'tampilUser.html',{'data':None})