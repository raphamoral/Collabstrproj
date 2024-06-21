from django.shortcuts import render
from django.http import JsonResponse
from .models import Content

from .utils import is_url_valid

def content_list(request):
    contents = Content.objects.all()
    valid_contents = [content for content in contents if is_url_valid(content.url)]
    content_data = [
        {
            'url': content.url,
            'is_video': content.url.endswith('.mp4'),
            'creator_name': content.creator.name,
            'creator_rating': content.creator.rating,
        }
        for content in valid_contents
    ]
    return render(request, 'content_list.html', {'contents': content_data})


def filter_content(request):
    platform = request.GET.get('platform', None)
    if platform:
        contents = Content.objects.select_related('creator').filter(creator__platform=platform)
    else:
        contents = Content.objects.select_related('creator').all()[:30]

    content_data = []
    for content in contents:
        content_data.append({
            'creator_name': content.creator.name,
            'creator_rating': content.creator.rating,
            'content_url': content.url,
            'is_video': content.url.endswith('.mp4')
        })

    return JsonResponse({'contents': content_data})