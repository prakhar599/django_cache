from django.shortcuts import render
from django.views.decorators.cache import cache_page

# @cache_page(30)
def home(request):
    return render(request,'perView/home.html')

def out(request):
    return render(request,'perView/out.html')
