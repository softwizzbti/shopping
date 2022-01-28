from shoppingsite.models import category

def category_list(request):
	category_list=category.objects.all()
	return {'cats':category_list }