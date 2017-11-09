from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):
	notice_author = serializers.CharField(read_only=True)
	class Meta:
		model = Api
		fields = ('id', 'notice_name', 'notice_desc', 'notice_author', 'notice_valid_till', 'notice_publish_date','year', 'branch', 'choices')

class AddNoticeSerializer(serializers.ModelSerializer):
	notice_author = serializers.CharField(read_only=True)
	class Meta:
		model = Api
		fields = ('id', 'notice_name', 'notice_desc', 'notice_author', 'notice_valid_till', 'notice_publish_date','year', 'branch','choices')

	def create(self, validated_data):
			return Api.objects.create(**validated_data)


class Notice_Year_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('year',)

class Notice_Branch_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('branch',)

class Notice_Branch_Year_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Api
		fields = ('branch', 'year')
