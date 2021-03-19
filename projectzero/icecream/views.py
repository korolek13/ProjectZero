from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ice_cream, User
from django.contrib.auth.decorators import login_required

def icecream_list(request):
    ice_cream_list = Ice_cream.objects.all()
    context = {
        'icecreams':ice_cream_list
    }
    return render(request, 'icecream/icecream-list.html', context)

@login_required
def icecream_detail(request, pk):
    ice_cream = get_object_or_404(Ice_cream, id=pk)
    name = ice_cream.name
    desc = ice_cream.description
    avatar = ice_cream.avatar
    price = ice_cream.price
    rating = ice_cream.rating
    context = {
        'name':name,
        'description':desc,
        'avatar':avatar,
        'price':price,
        'gold_rating':range(rating),
        'gray_rating':range(5-rating),
    }
    return render(request, 'icecream/icecream-detail.html', context)
