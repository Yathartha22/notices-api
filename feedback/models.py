from django.db import models
from django.contrib.auth import get_user_model

class FeedBack(models.Model):
	User = get_user_model()
	user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=50, null=False)
	description = models.TextField()