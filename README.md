# PythonLiveProject
Repo for my Python Live Project at The Tech Academy.

## Overview
My task for this project was to create a website that could allow a user to create items for a database, and allow them to edit or delete said items from the database. The user should also have the ability to view each item that has been inserted into the table. Along with that, I was assigned to implement an aAPI. I chose an API that would allow users to search for any anime title they wanted, and displyed their search results. The user could click on whichever search result they wanted and was directed to that results page on My Anime List. I also used Beautiful Soup to datascrape the My Anime List News section to display the lastest anime news to the user.

## Creating Items
![Create GIF](/GIFs/create.gif)
### Code
-[Template](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/templates/anime_reviews_create.html)
-[Form](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/forms.py)
-[Model](https://github.com/ryanwspears/PythonLiveProject/blob/main/AnimeReviews/AnimeReviews/models.py)
-View:
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

## Deleting Items
![Delete GIF](/GIFs/delete.gif)
### Code

## Searching For Anime
![Search GIF](/GIFs/search.gif)
### Code

## Getting News
![News GIF](/GIFs/news.gif)
### Code
