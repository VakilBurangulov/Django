from django.urls import path
from .views import index, top_sellers, advertisements

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement', advertisements, name='advertisements')
]