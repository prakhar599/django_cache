from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perSite/', include('perSite.urls')),
    path('perView/', include('perView.urls')),
    path('temp/', include('templateView.urls')),
    path('llca/', include('LLCA.urls')),
]
