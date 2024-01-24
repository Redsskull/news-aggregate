from django.core.paginator import Paginator
from django.shortcuts import render
import requests
from django.conf import settings


def home_page(request):
    api_key = settings.API
    r = requests.get(api_key)
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

    # pagination for 8 pages per page
    paginator = Paginator(news_list, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'news_list': page_obj})