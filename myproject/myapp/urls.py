from django.contrib import admin
from django.urls import path,include
from . import views
from .manager import cat_api, allCollection, singleCollection, catLook, look, articlelook, article

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.json_api, name='api'),
    path('categorie', cat_api, name='categorie'),

    # Les colections
    path('collection', allCollection, name='collection'),
    path('collection-single', singleCollection, name='collection_single'),

    # Les Look
    path('categorie-look', catLook, name='cat_look'),
    path('look', look, name='look'),
    path('look-article', articlelook, name='look_article'),

    #Les articles
    path('article', article, name='article'),

    path('apimodehomme/', views.json_mode_homme, name='apimodehomme'),
    path('json_detail_article/', views.json_detail_article, name='json_detail_article'),
    path('json_marques/', views.json_marques, name='json_marques'),

]