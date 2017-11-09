from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST

from django.http import Http404

from .serializers import (AccountSerializer, LoginSerializer, AdminRegisterSerializer,
	ProfileSerializer)
from .models import Account, Profile

# import jwt
# from rest_framework_jwt.utils import jwt_payload_handler

class AuthRegister(APIView):
	"""
	Register a new user.
	"""
	serializer_class = AccountSerializer
	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		allquery = Account.objects.all()
		serializer = AccountSerializer(allquery, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data,
					status=status.HTTP_201_CREATED)
		return Response(serializer.errors,
		status=status.HTTP_400_BAD_REQUEST)

# def create_token(user):
# 	payload = jwt_payload_handler(user)
# 	token = jwt.encode(payload, settings.SECRET_KEY)
# 	return token.decode('unicode_escape')


class AuthLogin(APIView):
	''' Manual implementation of login method '''

	permission_classes = (AllowAny,)
	serializer_class = LoginSerializer

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = LoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class AdminRegister(APIView):

	permission_classes = (AllowAny,)
	serializer_class = AdminRegisterSerializer

	def post(self, request, format=None):
		data = request.data
		serializer = AdminRegisterSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			new_data = serializer.data
			return Response(new_data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ProfileView(APIView):

	permission_classes = (IsAuthenticated,)
	serializer_class = ProfileSerializer
	queryset = Profile.objects.all()

	def get(self, request, format=None):
		current_user = request.user
		acc = Account.objects.filter(pk=current_user.pk)
		serializer = AccountSerializer(acc, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		param = request.data
		current_user = request.user
		if 'image' not in param:
			acc = Account.objects.filter(pk=current_user.pk)
			acc.update(username=param['username'], fullname=param['fullname'], email=param['email'], phonenumber=param['phone_no'])
			serializer = AccountSerializer(acc, many=True)
			return Response(serializer.data)
		else:
			try:
				# exist then update
				profile = Profile.objects.get(user=request.user)
				serializer = ProfileSerializer(profile, data=request.data, partial=True)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data)
				else:
					return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
			except Profile.DoesNotExist:
				# not exist then create
				serializer = ProfileSerializer(data=param)
				if serializer.is_valid():
					serializer.save(user=request.user)
					return Response(serializer.data)
				else:
					return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
