from django.contrib import admin
from django.urls import path
from aves_poultry.api_views import PoultryListView
from bovinos_cattle.api_views import CattleListView
from cerdos_swine.api_views import SwineListView
from equinos_equine.api_views import EquineListView

urlpatterns = [

    # ADMIN PANNEL SUPERUSER
    path('admin/', admin.site.urls),
    # Username: albertiaedev
    # Password: agrotech
    
    # API VIEWS
    path('api/poultry/', PoultryListView.as_view(), name='poultry-list'),

    path('api/cattle/', CattleListView.as_view(), name='cattle-list'),

    path('api/swine/', SwineListView.as_view(), name='swine-list'),

    path('api/equine/', EquineListView.as_view(), name='equine-list'),

]
