from django.shortcuts import redirect, render
from lists.models import Item, List
def home_page(request):
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/lists/the-only-list-in-the-world/')
	#return render(request, 'home.html')
	#items = Item.objects.all()	
	
	item_pribadi = ''
	if Item.objects.count() == 0:
		item_pribadi = "yey, waktunya berlibur"
	elif Item.objects.count() < 5:
		item_pribadi = "sibuk tapi santai"
	elif Item.objects.count() >= 5:
		item_pribadi = "oh tidak"
		

	return render(request, 'home.html', {'item_pribadi': item_pribadi})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	itemList = Item.objects.filter(list_id=list_id)

	item_pribadi = ''
	if itemList.count() == 0:
		item_pribadi="yey, waktunya berlibur"
	elif itemList.count() < 5:
		item_pribadi = "sibuk tapi santai"
	else:
		item_pribadi ="oh tidak"
	
	return render(request, 'list.html', {'list': list_, 'item_pribadi':item_pribadi})



def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request,list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
