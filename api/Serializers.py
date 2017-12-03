from rest_framework import serializers
from .models import Api
from accounts.models import Profile

class ApiSerializer(serializers.ModelSerializer):
	author_image = serializers.SerializerMethodField()
	notice_author = serializers.CharField(read_only=True)
	class Meta:
		model = Api
		fields = ('id' ,'notice_name', 'notice_desc', 'notice_file', 'notice_author', 'notice_valid_till',
			'notice_publish_date', 'year', 'branch', 'choices' , 'author_image')

	def get_author_image(self, instance):
		user_id = instance.user_id
		if user_id == None:
			return None
		try:
			image_url = Profile.objects.get(user=user_id).image.url
		except ProfileDoesNotExists:
			return None
		return image_url

class AddNoticeSerializer(serializers.ModelSerializer):
	notice_author = serializers.CharField(read_only=True)
	class Meta:
		model = Api
		fields = ('id' ,'notice_name', 'notice_desc', 'notice_file', 'notice_author', 'notice_valid_till',
			'notice_publish_date', 'year', 'branch', 'choices')

	def create(self, validated_data):
			return Api.objects.create(**validated_data)


class Notice_Year_Serializer(serializers.ModelSerializer):
	author_image = serializers.SerializerMethodField()

	class Meta:
		model = Api
		fields = ('year', 'author_image')

	def get_author_image(self, instance):
		user_id = instance.user_id
		if user_id == None:
			return None
		try:
			image_url = Profile.objects.get(user=user_id).image.url
		except ProfileDoesNotExists:
			return None
		return image_url

class Notice_Branch_Serializer(serializers.ModelSerializer):
	author_image= serializers.SerializerMethodField()

	class Meta:
		model = Api
		fields = ('branch', 'author_image')

	def get_author_image(self, instance):
		user_id = instance.user_id
		if user_id == None:
			return None
		try:
			image_url = Profile.objects.get(user=user_id).image.url
		except ProfileDoesNotExists:
			return None
		return image_url

class Notice_Branch_Year_Serializer(serializers.ModelSerializer):
	author_image= serializers.SerializerMethodField()

	class Meta:
		model = Api
		fields = ('branch', 'year', 'author_image')

	def get_author_image(self, instance):
		user_id = instance.user_id
		if user_id == None:
			return None
		try:
			image_url = Profile.objects.get(user=user_id).image.url
		except ProfileDoesNotExists:
			return None
		return image_url
