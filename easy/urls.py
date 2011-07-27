import urlparse, urllib

def add_params(url, params): 
    if isinstance(params, basestring):
        params = dict(urlparse.parse_qsl(params))
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)
