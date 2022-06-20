from django.shortcuts import render
from django.conf import settings
import requests

API_KEY = settings.API_KEY


def index(request):
    """ A view to return the index page """
    try:
        baseurl = 'https://api.thecatapi.com/'
        endpoint = 'v1/breeds'
        token = '57833af1-b126-472a-be08-be42f992da0b'

        headers = {'x-api-key': token}
        response = requests.get(
            baseurl + endpoint, headers=headers).json()

        print(response)

        for item in response:
            name = response[item]['name']
            image = response[item]['image']
            image_url = response[item]['image']['url']

        context = {
            'response': response,
            'name': name,
            'image': image,
            'image_url': image_url,
        }
        return render(request, 'index.html', context)
    except Exception:
        return render(request, 'index.html')
