from tutorial1.serializersnya import showUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

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