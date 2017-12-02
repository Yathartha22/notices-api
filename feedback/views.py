from django.shortcuts import render

from .serializers import FeedBackSerializer

from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class FeedBackView(APIView):

	permission_class = (IsAuthenticatedOrReadOnly,)

	def post(self, request, format=None):
		data = request.data
		current_user = request.user
		serializer = FeedBackSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save(user=current_user)
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
