from django.contrib import admin
from django.urls import include, path

from Content.views import content_list  # Certifique-se de usar 'Content' e não 'proj.Content'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', content_list, name='content_list'),

    path('content/', include('Content.urls')),
]