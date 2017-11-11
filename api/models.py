from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

class Api(models.Model):
	User = get_user_model()
	notice_name = models.CharField(max_length=20, null=True)
	notice_desc = models.TextField()
	notice_file = models.FileField(upload_to="accounts/notcie_files/", null=True, blank=True)
	notice_author = models.CharField(max_length=20, default='admin')
	notice_valid_till = models.DateTimeField(default=datetime.now, blank=True)
	notice_publish_date = models.DateTimeField(auto_now=True)
	year = models.CharField(max_length=5, null=True)
	branch = models.CharField(max_length=20, null=True)
	choices = models.CharField(max_length=20, null=True)
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=False,
		null=True
	)

	def __str__(self):
		return '%s' %self.notice_name
