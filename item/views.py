from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Item
from user_profile.models import Profile
from .form import ItemForm

def item_json(request, id):
    # ************ Notice ************
    # THIS METHOD IS REDUNDANT. IT IS NOT BEING USED AT ALL. 
    # REASON WHY IT IS STILL THERE IS BECAUSE I'M TOO SCARED TO REMOVE IT
    
    obj = get_object_or_404(Item, id=id)
    return JsonResponse({
        'id' : obj.id,
        'title' : obj.title,
        'description' : obj.description,
        'starting_price' : obj.starting_price,
        'seller' : {
            # data will be available publicly. Remember to remove some attributes
            'id' : obj.seller.id,
            'first_name' : obj.seller.user.first_name,
            'last_name' : obj.seller.user.last_name,
            'email' : obj.seller.user.email
            }
        })

def item_view(request, id):
    obj = get_object_or_404(Item, id=id)
    context = {
        'id' : id,
        'obj' : obj
    }
    return render(request, 'item/view_item.html', context)

@login_required
def add_item_form(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            current_profile = get_object_or_404(Profile, user=request.user)
            form.cleaned_data['seller'] = current_profile
            obj = Item.objects.create(**form.cleaned_data)
            return redirect('item_view', id=obj.id)
    context = {
        'form' : form
    }
    return render(request, 'item/add_item.html', context)