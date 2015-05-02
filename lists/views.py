from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.

def home(request):

    if(request.method == 'POST'):
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id))

    items = Item.objects.all()
    return render(request, 'lists/home.html')

def list(request, list_id):

    if(request.method == 'POST'):
        list_ = List.objects.get(id=list_id)
        item = Item.objects.create(text=request.POST['item_text'], list=list_)
        items = Item.objects.filter(list=list_)
        return render(request, 'lists/list.html', {'items': items,
            'list': list_})

    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'items': items, 'list': list_})
