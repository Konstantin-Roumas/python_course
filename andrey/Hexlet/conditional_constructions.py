def normalize_url(url):
    if url[:8] == 'https://':
        return url
    elif url[:7] == 'http://':
        url = 'https:' + url[5:]
    else:
        url = 'https://' + url
    return url


print(normalize_url('http://google.com'))
