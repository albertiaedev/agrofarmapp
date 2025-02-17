from django.contrib import admin
from django.urls import path
from aves.api_views import AvesView
from bovinos.api_views import BovinosView
from cerdos.api_views import CerdosView
from equinos.api_views import EquinosView

urlpatterns = [

    # ADMIN PANNEL SUPERUSER
    path('admin/', admin.site.urls),
    # Username: albertiaedev
    # Password: agrotech
    
    # API VIEWS
    path('api/aves/', AvesView.as_view(), name='lista-aves'),

    path('api/bovinos/', BovinosView.as_view(), name='lista-bovinos'),

    path('api/cerdos/', CerdosView.as_view(), name='lista-cerdos'),

    path('api/equinos/', EquinosView.as_view(), name='lista-equinos'),

]
