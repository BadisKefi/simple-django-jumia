from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('first.html')
    context = {
        'nom': 'Guerbouj',  # écrire votre nom ici
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def jumia_scraper(request):
    url = "https://www.jumia.com.tn/smartphones/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []
    for product in soup.findAll('article', {'class': 'prd _box _hvr'}):
        name = product.find('div', {'class': 'name'}).get_text()
        price = product.find('div', {'class': 'prc'}).get_text()
        image = product.find('img', {'class': 'img'}).get('data-src')
        products.append({'name': name, 'price': price, 'image': image})
    return render(request, 'products.html', {'products': products})
