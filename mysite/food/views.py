from django.shortcuts import render
from django.http import HttpResponse
from.models import Item
from django.template import loader #To load html templates

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
    