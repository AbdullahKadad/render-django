import os
import requests
from django.shortcuts import render, get_object_or_404
from .models import Image
from dotenv import load_dotenv

load_dotenv()

PIXABAY_API_KEY = os.getenv('PIXABAY_API_KEY')

def fetch_pixabay_data():
    if not Image.objects.exists():  # Check if data already exists in the database
        url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q=food&category=food"
        response = requests.get(url)
        data = response.json()
        for hit in data['hits']:
            Image.objects.create(
                pixabay_id=hit['id'],
                tags=hit['tags'],
                preview_url=hit['previewURL'],
                large_image_url=hit['largeImageURL'],
                views=hit['views'],
                downloads=hit['downloads'],
                likes=hit['likes'],
                comments=hit['comments'],
                user=hit['user'],
                user_image_url=hit['userImageURL'],
            )

def image_list(request):
    fetch_pixabay_data()  # Ensure data is fetched once
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {'image': image})