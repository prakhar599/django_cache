from django.urls import path
from django.conf.urls import include
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('home/', cache_page(30)(views.home)),
    path('out/', views.out),
    #  path('foo/<int:code>/', cache_page(60 * 15)(my_view)),

]
