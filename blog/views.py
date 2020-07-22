from django.shortcuts import render

from blog.models import Article, Author


def frontend(request):
    """Vue.js will take care of everything else."""
    articles = Article.objects.all()
    authors = Author.objects.all()

    data = {
        'articles': articles,
        'authors': authors,
    }

    return render(request, 'template.html', data)
