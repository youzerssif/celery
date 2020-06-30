from django.contrib import admin
from django.urls import path,include
from . import views
from .manager import cat_api, collection_api, data_collection

app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.json_api, name='api'),
    path('categorie', cat_api, name='categorie'),
    path('collection', collection_api, name='collection'),
    path('collection-data', data_collection, name='collection_data'),
    path('apimodehomme/', views.json_mode_homme, name='apimodehomme'),

]