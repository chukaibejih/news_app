from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):    

    # Init
    newsapi = NewsApiClient(api_key='732645287800430b802c5ddad7eadbb8')

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(language='en',country='ng')

    articles = top_headlines['articles']

    # articles_list = articles.objects.all()
    # page = request.GET.get('page', 1)

    # paginator = Paginator(articles_list, 10)
    # try:
    #     articles = paginator.page(page)
    # except PageNotAnInteger:
    #     articles = paginator.page(1)
    # except EmptyPage:
    #     articles = paginator.page(paginator.num_pages)

    image = [] 
    title = []
    description = []
    article = []
    article_url = []
    published_at = []
    # category = []

    for i in range(len(articles)):
        image.append(articles[i]['urlToImage'])
        title.append(articles[i]['title'])
        description.append(articles[i]['description'])
        article.append(articles[i]['content'])
        article_url.append(articles[i]['url'])
        published_at.append(articles[i]['publishedAt'])
        # category.append(articles[i]['category'])
        

    my_news = zip(image, title, description, article, article_url, published_at)

    return render(request, 'news/index.html', context = {"my_news":my_news})

