from django.shortcuts import render, get_object_or_404
from .models import Author, Post

# Create your views here.

def MainPage(request):
    return render(request, 'BD/MainPage.html', {'title': 'Главная страница'})


class NewsView():
    # Передача Содержания автора даты и тд
    @classmethod
    def ShowNews(cls, request):
        posts = Post.objects.all().order_by('-date')
        avtor = Author.objects.all()
        return render(request, 'BD/AllNews.html', {'posts': posts,
                                                   'avtor': avtor,
                                                   'title': 'Новости'
                                                   })

    # Вызывает шаблон для страницы с Полной инфорпацией о любом посте
    @classmethod
    def Post_detal(cls, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'BD/PostDetal.html', {'post': post})