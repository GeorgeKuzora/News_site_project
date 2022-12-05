from django import forms
from news_board.models import News, Commentaries
from django.forms import Textarea


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'tag']


class CommentariesForm(forms.ModelForm):
    # user_name = forms.CharField(required=False, help_text='Имя незарегистрированого пользователя')
    # commentary = forms.CharField(widget=forms.Textarea, required=True, help_text='Текст комментария')
    # connected_news = forms.CharField(widget=forms.Select, required=True, help_text='Новость')
    # user = forms.CharField(widget=forms.Select, required=False, help_text='Имя зарегистрированого пользователя')
    class Meta:
        model = Commentaries
        fields = '__all__'
        widgets = {
                    'commentary': Textarea(),
                }
# class AuthenticatedUserCommentariesForm(forms.ModelForm):
#     class Meta:
#         model = Commentaries
#         fields = '__all__'
#         widgets = {'user_name': forms.HiddenInput(),
#                    'connected_news': forms.HiddenInput(),
#                    'user': forms.HiddenInput(),
#                 }
#
# class NotAuthenticatedUserCommentariesForm(forms.ModelForm):
#     class Meta:
#         model = Commentaries
#         fields = '__all__'
