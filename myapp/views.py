from pickle import TRUE
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from myapp.models import News
from myapp.serializers import NewsSerializer

@api_view(["GET"])
def news_view(request):
    url = 'https://feeds.npr.org/1004/feed.json'
    news =requests.get(url).filter.order_by('-id')[:5]
    news_serializer=NewsSerializer(news,many=True)
    # dat =response.json()["data"]
    # print(data)
    return Response(news_serializer.data)