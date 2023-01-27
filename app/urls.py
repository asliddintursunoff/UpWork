from django.urls import path, include

from app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',menu.as_view(), name='menu'),
    path('workers/',WorkerView.as_view(), name='workers'),
    path('workersabout/',WorkersView.as_view(), name='workers_about'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)