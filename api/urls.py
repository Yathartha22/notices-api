from django.conf.urls import url
from .views import (AddNotice, ApiViewSet, NoticeYear, NoticeBranch,
	NoticeBranchYear, YourNotices, DeleteNotice)

urlpatterns = [
	url(r'^addnotices/$', AddNotice.as_view()),
	url(r'^deleteNotices/$', DeleteNotice.as_view()),
	url(r'^notices/$', ApiViewSet.as_view()),
	url(r'^notices/year/', NoticeYear.as_view()),
	url(r'^notices/branch/', NoticeBranch.as_view()),
	url(r'^notices/branchyear/', NoticeBranchYear.as_view()),
	url(r'^notices/yournotices/', YourNotices.as_view()),
]
