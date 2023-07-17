from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader #To load html templates
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()

    '''
    Django looks for templates in an app-specific templates folder or a project-level templates folder.
    If your app is food, index.html file must be located in food/templates/food/index.html.
    Following is used to load template and pass in HttpResponse. No need with render.
    '''
    # template = loader.get_template('food/index.html')                                                    

    context = { #Django combines data from DB and the template, and then returns a combined output called context.
            'item_list' : item_list, #context is used to obtain data from DB
    }
    # return HttpResponse(template.render(context, request)) # context is passed to template(index.html) 

    return render(request, 'food/index.html', context) # No need to create template variable while using render

def item(request):
    return HttpResponse('<h1>This is an item view</h1>') # HTML can also be passed

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid(): # Checks if data submitted is valid
        form.save()
        return redirect('food:index') #redirect function redirects to a particular page

    return render(request, 'food/item-form.html', {'form':form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form':form, 'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        print('hi') 
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})
     