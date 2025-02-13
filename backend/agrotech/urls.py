from django.contrib import admin
from django.urls import path, include
from aves_poultry.api_views import PoultryListView

urlpatterns = [

    # ADMIN PANNEL SUPERUSER
    path('admin/', admin.site.urls),
    # Username: albertiaedev
    # Password: agrotech
    
    # API VIEWS
    path('api/poultry/', PoultryListView.as_view(), name='poultry-list'),
    path('', include('aves_poultry.urls')),

]
