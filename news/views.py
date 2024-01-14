from django.core.paginator import Paginator
from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

def index(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=b967fff93412e1192e8a083ff64ed643&languages=en')
    res = r.json()
    data = res.get('data', [])

    news_list = []
    for i in data:
        title = i.get('title', '')
        description = i.get('description', '')
        image = i.get('image', '')
        url = i.get('url', '')
        published_at = i.get('published_at', '')

        news_list.append((title, description, image, url, published_at))

    #pagination for 10 pages per page
    paginator = Paginator(news_list, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/index.html', {'news_list': page_obj})



