from django.http import HttpResponse
from django.shortcuts import render
import validators
from django.db import models
from .models import *
from urlshortener.models import Shortener
from django.contrib.auth.models import User


def newurl(request):
   if request.method == 'GET':
      return render(request, 'home.html')
   if request.method == 'POST':
      long_url = request.POST["long_url"]
      if validators.url(long_url):
         s = Shortener(long_url=long_url, author=User.objects.get(id=request.user.id))
         s.save()
         short = s.short_url
         short_url = request.build_absolute_uri('/') + short
         dict = {
            'long_url': long_url,
            'short_url': short_url
         }
         return render(request, 'newurl.html', dict)
      else:
         return render(request, 'home.html', dict)


def mylinks(request):
   Links = Shortener.objects.filter(author=User.objects.get(id=request.user.id))
   dict = {
            'links': Links,
            'baseurl': request.build_absolute_uri('/'),
         }
   print(Links)
   return render(request, 'mylinks.html', dict)