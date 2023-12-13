from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import never_cache



def home(request):
    mk =  cache.get('my_key','has_expired')
    if mk == 'has_expired' :
        print('hi')
        cache.set('mykey','hello prakhar',60)
        mk= cache.get('my_key')
    print(mk)
    return render(request,'LLCA/home.html',{'mk':mk})
