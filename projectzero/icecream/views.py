from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ice_cream, User, Follow
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def icecream_list(request):
    ice_cream_list = Ice_cream.objects.all()
    paginator = Paginator(ice_cream_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page':page,
        'paginator':paginator
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
    if request.user.is_authenticated:
        is_favourite = Ice_cream.objects.filter(users__username=request.user.username, pk=pk).exists()
    else:
        is_favourite = False
    context = {
        'name':name,
        'description':desc,
        'avatar':avatar,
        'price':price,
        'gold_rating':range(rating),
        'gray_rating':range(5-rating),
        'is_favourite':is_favourite,
        'pk':pk
    }
    return render(request, 'icecream/icecream-detail.html', context)

def profile_follow(request, username):
    user = get_object_or_404(User, username=username)
    if user != request.user:
        Follow.objects.get_or_create(user=request.user, author=user)
    return redirect('profile', username=user)
    
def profile_unfollow(request, username):
    user = get_object_or_404(User, username=username)
    Follow.objects.filter(user=request.user, author=user).delete()
    return redirect('profile', username=user)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    ice_cream_list = user.ice_cream_set.all()
    count_ice_cream = len(user.ice_cream_set.all())
    print(ice_cream_list)
    #ice_cream_listid = user.icecream_favourite.filter(id_user=user)
    #ice_cream_list = Ice_cream.objects.filter(pk=ice_cream_listid)
    paginator = Paginator(ice_cream_list, 1)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(user=request.user, author=user).exists()
    else:
        is_following = False
    context = {
        'username':user,
        'page':page,
        'paginator':paginator,
        'is_following':is_following,
        'count':count_ice_cream
    }
    return render(request, 'profile.html', context)

def favourite_follow(request, pk):
    ice_cream = get_object_or_404(Ice_cream, pk=pk)
    user = get_object_or_404(User, username=request.user.username)
    print(request.user.username)
    user.ice_cream_set.add(ice_cream)
    #Favourite_icecream.objects.get_or_create(id_user=request.user, id_icecream=ice_cream)
    return redirect('detail', pk=pk)
    
def favourite_unfollow(request, pk):
    ice_cream = get_object_or_404(Ice_cream, pk=pk)
    user = get_object_or_404(User, username=request.user.username)
    user.ice_cream_set.remove(ice_cream)
    #Favourite_icecream.objects.filter(id_user=request.user, id_icecream=ice_cream).delete()
    return redirect('detail', pk=pk)