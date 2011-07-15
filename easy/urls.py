from urlparse import urlparse, urlunparse 
from urllib import urlencode

def add_params(url, **params): 
    """ don't just add the **params because the url 
    itself might contain CGI variables embedded inside 
    the string. """ 
    url_parsed = list(urlparse(url))

    encoded = urlencode(params) 
    qs = url_parsed[4] 
    if encoded: 
        if qs: 
            qs += '&'+encoded 
        else: 
            qs = encoded 
    netloc = url_parsed[1] 
    if netloc.find('?')>-1: 
        url_parsed[1] = url_parsed[1][:netloc.find('?')] 
        if qs: 
            qs = netloc[netloc.find('?')+1:]+'&'+qs 
        else: 
            qs = netloc[netloc.find('?')+1:]

    url_parsed[4] = qs

    url = urlunparse(url_parsed) 
    return url 
