from django.urls import path
from . import views


urlpatterns = [
# сслыка на представление с заглавной страницей
    path('',views.NewsListView.as_view(), name='news'),
# ссылка на представление с детальной страницей новости
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_details'),
# ссылка на представление с созданием новости
    path('post/', views.NewNewsFormView.as_view(), name='news_post'),
# ссылка на предсталвение с редактированием новости
    path('post/<int:pk>/edit/', views.NewsFormView.as_view(), name='edit_post'),
# ссылка на предсталвение с комментариями к новости
    # path('news/<int:news_id>', views.CommentaryListView.as_view(), name='comments'),
    # path('post_comment/', views.NewCommentaryFormView.as_view(), name='commentary_post'),
]
