from django.shortcuts import render
from django.http import HttpResponse
import feedparser
# Create your views here.


def home(request):
    url = "https://www.instagram.com/explore"
    feed = feedparser.parse(url)

    return HttpResponse(feed.feed.description)