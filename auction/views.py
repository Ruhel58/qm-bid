from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Auction
from user_profile.models import Profile
from .form import AuctionForm
from item.models import Item
import json

def all_auction_json(request):
    # get the last 10 auction records
    # if the number of records are less than 10, get them all
    obj_dict = {'auctions' : []}
    objects = Auction.objects.all()
    if Auction.objects.count() >= 10:
      objects = objects.order_by('-id')[:10]
          
    for obj in objects:
        obj_dict['auctions'].append(obj.to_dict())
    
    obj_json = json.loads(
        json.dumps(obj_dict)
    )

    return JsonResponse(obj_json)

def home_view(request):
    obj = Auction.objects.filter(active = True)
   
    if obj.count() >= 10:    
        obj = obj.order_by('-id')[:10]

    context = {
        'obj' : obj
    }
    return render(request, 'auction/home_view.html', context)


def auction_json(request, id):
    obj = get_object_or_404(Auction, id=id)
    obj.update_active()

    obj_dict = obj.to_dict()
    obj_json = json.loads(
        json.dumps(obj_dict)
    )
    return JsonResponse(obj_json)


def auction_view(request, id):
    # The parameter of the URL is passed into html file via context.
    # ID will be used for dynamic url.
    object = get_object_or_404(Auction, id=id)
    object.update_active()
    context = {
        'obj' : object,
        'id' : id,

    }
    return render(request, 'auction/view_auction_listing.html', context)

def all_auctions(request):
    obj = Auction.objects.all()
    context = {
        'obj' : obj
    }

    return render(request, 'auction/view_all_auctions.html', context)

@login_required
def add_auction_view(request):
    current_profile = get_object_or_404(Profile, user=request.user)
    form = AuctionForm(user=current_profile)
    if request.method == 'POST':
        form = AuctionForm(request.POST, user=current_profile)
        if form.is_valid():
            form.cleaned_data['seller'] = current_profile
            obj = Auction.objects.create(**form.cleaned_data)
            return redirect('auction_view', id=obj.id)


    context = {
        'form' : form
    }
    return render(request, 'auction/add_auction.html', context)

@login_required
def set_bid(request, id):
    obj = get_object_or_404(Auction, id=id)
    obj.update_active()
    if request.method =='POST':
        user_bid = float(request.POST['current_bid'])
        user_profile = Profile.objects.filter(user__username=request.POST['username'])[0]
        
        if user_bid <= obj.item.starting_price or user_bid <= obj.current_bid:
            return JsonResponse({
                'success' : False,
                'message' : 'The bid is less than the minimum bid'
                })
        
        obj.current_bid = user_bid
        obj.highest_bidder = user_profile
        obj.save()

        return JsonResponse({
            'success' : True,
            'message' : 'Current bid price updated in the server'
        })


def search(request):
    print("query started")
    if request.method=='POST':
        res_dict = {'results' : []}
        query = request.POST['query']
        results = Auction.objects.filter(item__title__contains=query)
        if not results:
            return JsonResponse({'results' : []})
    else:
        query = ''
  
    results = Auction.objects.filter(item__title__contains=query)

    context = {
        'obj' : results
    }
    for result in results:
        result.update_active()
        res_dict['results'].append(result.to_dict())

    res_json = json.loads(
        json.dumps(res_dict)
    )
    
    return JsonResponse(res_json)




