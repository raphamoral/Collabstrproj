import requests
from django.core.cache import cache

def is_url_valid(url):
    cache_key = f"url_validity_{url}"
    cached_result = cache.get(cache_key)

    if cached_result is not None:
        return cached_result

    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('content-type', '').lower()
        is_valid = response.status_code == 200 and ('image' in content_type or 'video' in content_type)
    except requests.RequestException:
        is_valid = False

    cache.set(cache_key, is_valid, timeout=60*60)  # Cache result for 1 hour
    return is_valid