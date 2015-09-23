from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')
	items = Item.objects.all()	
	
	#item_pribadi = ''
	#if Item.objects.count() == 0:
	#	item_pribadi = "yey, waktunya berlibur"
	#elif Item.objects.count() < 5:
	#	item_pribadi = "sibuk tapi santai"
	#elif Item.objects.count() >= 5:
	#	item_pribadi = "oh tidak"
		

	return render(request, 'home.html', {'items': items})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
