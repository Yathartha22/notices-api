from django.shortcuts import render
from .models import Api
from accounts.models import Account
from rest_framework import viewsets
from rest_framework.views import APIView
from .Serializers import (ApiSerializer, AddNoticeSerializer, Notice_Year_Serializer,
	Notice_Branch_Serializer, Notice_Branch_Year_Serializer)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class ApiViewSet(APIView):

	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = ApiSerializer
	def get(self, request, format=None):
		queryset = Api.objects.all().order_by('-notice_publish_date')
		serializer = ApiSerializer(queryset, many=True)
		return Response(serializer.data)

class AddNotice(APIView):

	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = AddNoticeSerializer
	def post(self, request, format=None):
		data = request.data
		current_user = request.user
		author_name = Account.objects.get(pk=current_user.pk).fullname
		serializer = AddNoticeSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			serializer.validated_data['notice_author'] = author_name
			serializer.save(user=current_user)
			new_data = serializer.data
			return Response(new_data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class NoticeYear(APIView):
	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = Notice_Year_Serializer

	def post(self, request, format=None):
		param = request.data
		queryset = Api.objects.filter(year=param["year"], branch=None)
		serializer = ApiSerializer(queryset, many=True)
		return Response(serializer.data)

class NoticeBranch(APIView):
	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = Notice_Branch_Serializer
	def post(self, request, format=None):
		param = request.data
		queryset = Api.objects.filter(branch = param["branch"], year=None)
		serializer = ApiSerializer(queryset, many=True)
		return Response(serializer.data)

class NoticeBranchYear(APIView):
	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = Notice_Branch_Year_Serializer

	def post(self, request, format=None):
		param = request.data
		queryset = Api.objects.filter(branch=param['branch'], year=param['year'])
		serializer = ApiSerializer(queryset, many=True)
		return Response(serializer.data)

class YourNotices(APIView):
	permission_class = (IsAuthenticatedOrReadOnly,)
	serializer_class = ApiSerializer

	def get(self, request, format=None):
		current_user =  request.user
		queryset = Api.objects.filter(user=current_user.pk).order_by('-notice_publish_date')
		serializer = ApiSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		data = request.data
		try:
			# pk will be additional field that will be provided at the frontend.
			pk = data['pk']
			notice = Api.objects.get(pk=pk)
			serializer = ApiSerializer(notice, data=data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
		except Api.DoesNotExist:
			return Response("The notice does not exists")
