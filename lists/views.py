from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.

def home_page(request):
    items = Item.objects.all()
    return render(request, 'lists/home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list/')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})
