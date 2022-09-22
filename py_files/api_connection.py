# David Harianto

import requests, random

def get_list(season, year, id):
    api_url = "https://api.myanimelist.net/v2/anime/season/" + year + "/" + season.lower() + "?limit=20&sort=anime_num_list_users&fields=genres"
    response = requests.get(api_url, headers = {
        'X-MAL-CLIENT-ID': id
        })

    list = response.json()
    response.close()

    # appends anime titles to list
    anilist = []
    img_list = []
    genres = []
    for anime in list['data']:
        anilist.append(anime['node']['title'])
        img_list.append(anime['node']['main_picture']['medium'])
        genres.append(anime['node']['genres'])
    list = response.json()
    response.close()

    return anilist, img_list, genres