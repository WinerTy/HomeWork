from django.urls import path
from . import views
from .views import NewsView

urlpatterns = [
    path('main/', views.MainPage, name='main'),
    path('news/', NewsView.ShowNews, name='news'),
    path('news/<int:post_id>/', NewsView.Post_detal, name='Post Details')
]