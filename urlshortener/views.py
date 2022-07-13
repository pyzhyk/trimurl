from django.shortcuts import render
from urlshortener.models import Shortener
from django.http import Http404, HttpResponse, HttpResponseRedirect


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.follows += 1
        shortener.save(s=True)
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        return render(request, '404.html')

