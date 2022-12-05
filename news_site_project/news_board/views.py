from os import wait
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from news_board.models import News, Commentaries
from news_board.forms import NewsForm, CommentariesForm
from django.contrib.auth.models import User
from app_users.forms import AuthForm
from app_users.models import Profile
from django.core.exceptions import PermissionDenied

# Create your views here.
# Создание преставление заглавной старницы
class NewsListView(ListView):
    model = News
    context_object_name = 'news'


class NewsDetailView(View):

    def get(self, request, pk):
        detailed_news = News.objects.get(pk=pk)
        current_user = request.user
        commentary_data = {
                'connected_news': detailed_news,
                'user': current_user
                }
        commentaries_form = CommentariesForm(commentary_data)
        return render(request, 'news_board/news_detail.html', context={'detailed_news': detailed_news, 'commentaries_form': commentaries_form, 'pk': pk, 'current_user': current_user})

    def post(self, request, pk):
        detailed_news = News.objects.get(pk=pk)
        commentaries_form = CommentariesForm(request.POST)
        if commentaries_form.is_valid():
            Commentaries.objects.create(**commentaries_form.cleaned_data)
            return HttpResponseRedirect(f'/news/{pk}')
        return render(request, 'news_board/news_detail.html', context={'detailed_news': detailed_news, 'commentaries_form': commentaries_form, 'pk': pk})


class CommentaryListView(ListView):
    model = Commentaries
    context_object_name = 'comments'


class NewNewsFormView(View):
    def get(self, request):
        user = request.user
        user_profile = Profile.objects.get(user=user)
        verification = user_profile.verification_mark
        if not verification:
            raise PremissionDenied()
        news_form = NewsForm()
        return render(request, 'news_board/post.html', context = {'news_form': news_form})

    def post(self, request):
        user = request.user
        user_profile = Profile.objects.get(user=user)
        verification = user_profile.verification_mark
        if not verification:
            raise PremissionDenied()
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return HttpResponseRedirect('/')
        return render(request, 'news_board/post.html', context = {'news_form': news_form})
# Создание представления редактирования новости
class NewsFormView(View):
    def get(self, request, news_id):
        one_news = News.ofjects.get(id=news_id)
        news_form = NewsForm(instance=one_news)
        return render(request, 'news_board/edit.html', context = {'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        one_news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=one_news)

        if news_form.is_valid():
            one_news.save()
            return render(request, 'news_board/edit.html', context = {'news_form': news_form, 'news_id': news_id})


class NewCommentaryFormView(View):
    def get(self, request):
        commentaries_form = CommentariesForm()
        return render(request, 'news_board/post_comment.html', context = {'commentaries_form': commentaries_form})

    def post(self, request):
        commentaries_form = CommentariesForm(request.POST)

        if commentaries_form.is_valid():
            commentaries_form.save()
            return HttpResponseRedirect('/')
        return render(request, 'news_board/post_comment.html', context = {'commentaries_form': commentaries_form})
