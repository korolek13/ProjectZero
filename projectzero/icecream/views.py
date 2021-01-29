from django.shortcuts import render
from django.http import HttpResponse
from .models import icecream_db

def icecream_list(request):
    icecreamnames = []
    for i in range(len(icecream_db)):
        temp = icecream_db[i]
        desc = ''
        for j in range(len(icecream_db[i]['description'])):
            desc += icecream_db[i]['description'][j] + ' '
        temp['index'] = i
        temp['desc'] = desc
        icecreamnames.append(temp)
        #icecreamnames += f"<a href = '{i}/'>{icecream_db[i]['name']} </a> <br>"
    context = {
        'icecreams':icecreamnames
    }
    return render(request, 'icecream/icecream-list.html', context)

def icecream_detail(request, pk):
    desc = ''
    for i in range(len(icecream_db[pk]['description'])):
        desc += f" <li>{icecream_db[pk]['description'][i]}</li>"
    name = icecream_db[pk]['name']
    #desc = icecream_db[pk]['description'] 
    avatar = icecream_db[pk]['avatar']
    context = {
        'name':name,
        'description':desc,
        'avatar':avatar,
    }
    return render(request, 'icecream/icecream-detail.html', context)
