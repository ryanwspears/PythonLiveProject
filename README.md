# PythonLiveProject
Repo for my Python Live Project at The Tech Academy.

## Overview
My task for this project was to create a website that could allow a user to create items for a database, and allow them to edit or delete said items from the database. The user should also have the ability to view each item that has been inserted into the table. Along with that, I was assigned to implement an aAPI. I chose an API that would allow users to search for any anime title they wanted, and displyed their search results. The user could click on whichever search result they wanted and was directed to that results page on My Anime List. I also used Beautiful Soup to datascrape the My Anime List News section to display the lastest anime news to the user.

## Creating Items
![Create GIF](/GIFs/create.gif)
### Code
- [Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_create.html)
- [Form](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/forms.py)
- [Model](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/models.py)
- View:
```cs
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
```

## Editing Items
![Edit GIF](/GIFs/edit.gif)
### Code
- [Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_edit.html)
- View:
```cs
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
 ```

## Deleting Items
![Delete GIF](/GIFs/delete.gif)
### Code
- [Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_delete.html)
- View:
```cs
def anime_reviews_delete(request, pk):
    item = get_object_or_404(Anime, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('anime_reviews_view')
    context = {'item': item}
    return render(request, 'anime_reviews_delete.html', context)
 ```

## Searching For Anime
![Search GIF](/GIFs/search.gif)
### Code
- [Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_api.html)
- View:
```cs
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
 ```

## Getting News
![News GIF](/GIFs/news.gif)
### Code
- [Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_news.html)
- View:
```cs
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
 ```
