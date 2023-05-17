from endpoint.serializers import showUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse, HttpResponse

@api_view(['GET','POST'])
def viewAllUser(request):
	if request.method == "GET":
		usernya = User.objects.all()
		myuser = showUser(usernya, many=True)
		return Response(myuser.data)

	elif request.method == "POST":
		myuser = showUser(data=request.data)
		if myuser.is_valid():
			myuser.save()
			return Response(request.data,status=200)
		return Response(myuser.errors,status=400)

@api_view(['GET','DELETE','UPDATE'])
def viewDetailUser(request,pk):
	if request.method == "GET":
		try:
			usernya = User.objects.get(id=pk)
			myuser = showUser(usernya)
			return Response(myuser.data)
		except:
			return Response(status=404)
	
	if request.method=="DELETE":
		try:
			User.objects.get(id=pk).delete()
		except:
			Response(status=404)

		usernya = User.objects.all()
		if(usernya.count()>1):
			myuser = showUser(usernya,many=True)
			return Response(myuser.data)
		else:
			myuser = showUser(usernya)
			return Response(myuser.data)

