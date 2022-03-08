from django.shortcuts import render, get_object_or_404
from .models import Article, info
from django.views.generic import ListView, DetailView

class ArticleList(ListView):
	queryset = Article.objects.all().order_by("-time")[0:4]
	template_name = "article/article.html"

class ArticleSList(ListView):
	queryset = Article.objects.filter(status=True).order_by("-time")
	template_name = "article/articles.html"

class ArticleDetailView(DetailView):
	template_name = "article/articledetail.html"

	def get_queryset(self):
		global articles
		slug = self.kwargs.get("slug")
		articles = get_object_or_404(Article, slug=slug)
		return Article.objects.filter(slug=slug)

	def get_context_data(self, **kwargs):
		context =  super().get_context_data(**kwargs)
		context["articles"] = articles
		return context

class InfoList(ListView):
	model = info
	template_name = "article/info.html"