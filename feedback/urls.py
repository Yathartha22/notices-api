from django.conf.urls import url

from .views import FeedBackView

urlpatterns =[
	url(r'^feedback/$', FeedBackView.as_view()),
]
