from django.urls import path
from .views import ArticleList, InfoList, ArticleDetailView, ArticleSList

app_name = "mysite"

urlpatterns = [
	path("", ArticleList.as_view(), name="Article"),
	path("Article/", ArticleSList.as_view(), name="ArticleS"),
	path("detail/<slug:slug>/",ArticleDetailView.as_view(), name="detail"),
	path("rezomie/", InfoList.as_view(), name="infos"),
]