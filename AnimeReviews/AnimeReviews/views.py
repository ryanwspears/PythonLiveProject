import requests
import json
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewAnime
from .models import Anime


def anime_reviews_home(request):
    return render(request, "anime_reviews_home.html")


def anime_reviews_create(request):
    form = NewAnime(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('anime_reviews_create')
    else:
        print(form.errors)
        form = NewAnime()
        context = {'form': form}
    return render(request, 'anime_reviews_create.html', context)


def anime_reviews_view(request):
    view = Anime.objects.all()
    return render(request, 'anime_reviews_view.html', {'view': view})


def anime_reviews_details(request, pk):
    details = get_object_or_404(Anime, pk=pk)
    context = {'details': details}
    return render(request, 'anime_reviews_details.html', context)


def anime_reviews_edit(request, pk):
    item = get_object_or_404(Anime, pk=pk)
    form = NewAnime(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('anime_reviews_view')

        else:
            print(form.errors)
    else:
        return render(request, 'anime_reviews_edit.html', {'form': form, 'item': item})


def anime_reviews_delete(request, pk):
    item = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('anime_reviews_view')
    context = {'item': item}
    return render(request, 'anime_reviews_delete.html', context)


def anime_reviews_api(request):

    resultList = []

    if request.method == 'POST':
        url = "https://jikan1.p.rapidapi.com/search/anime"

        querystring = {"q": request.POST['searchTerm']}

        headers = {
            'x-rapidapi-host': "jikan1.p.rapidapi.com",
            'x-rapidapi-key': "daa3c3b9d7mshaa4e1ceb0660c2dp1caa26jsn9495166557eb"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        result = json.loads(response.text)

        for i in result['results']:
            url = i['url']
            img_url = i['image_url']
            title = i['title']
            resultArray = (url, img_url, title)
            resultList.append(resultArray)

    context = {
        'resultList': resultList
    }

    return render(request, 'anime_reviews_api.html', context)


def anime_reviews_news(request):

    feed = []

    page = requests.get("https://myanimelist.net/news")

    soup = BeautifulSoup(page.content, 'html.parser')

    news = soup.find('div', class_="js-scrollfix-bottom-rel")

    newsItems = news.find_all(class_="news-unit clearfix rect")

    for i in newsItems:
        title = i.find(class_="title").get_text()
        img = i.img["src"]
        link = i.a["href"]
        desc = i.find(class_="text").get_text()
        newsArray = (title, img, link, desc)
        feed.append(newsArray)

    context = {
        'feed': feed
    }

    return render(request, 'anime_reviews_news.html', context)
