from django.shortcuts import render
from .models import NewsArticle
from .forms import CrawlForm
from .commands.crawl_news import crawl_news

def crawl_and_show_news(request):
    if request.method == 'POST':
        form = CrawlForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            page_number = form.cleaned_data['page_number']

            articles = crawl_news(keyword, page_number)

            return render(request, 'newsapp/news_list.html', {'articles': articles, 'form': form})
    else:
        form = CrawlForm()
    return render(request, 'newsapp/form.html', {'form': form})
