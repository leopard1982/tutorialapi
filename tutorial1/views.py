from django.shortcuts import render, HttpResponse, redirect
import requests
from tutorial1.forms import inputUser

# Create your views here.
def hello_world(request):
	return render(request,'hello_world.html')

def tampilUser(request):
	myreq = requests.get("http://192.168.1.50:8787/api/1/")

	try:
		return render(request,'tampilUser.html',{'data':myreq.json()})
	except:
		return render(request,'tampilUser.html',{'data':None})

def hapusUser(request,username):
	myreq = requests.delete("http://192.168.1.50:8787/api/1/" + username + "/")
	return redirect('tampilUser')

def addUser(request):
	if request.method=="POST":
		print(request.POST['username'])
		print(request.POST['email'])
		data = {'username': request.POST['username'],'email':request.POST['email']}
		print(data)
	inputnya = inputUser()
	return render(request,'inputuser.html',{'forms':inputnya})