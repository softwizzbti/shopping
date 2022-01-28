from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from shoppingsite.models import contact,products,genre,category,subcategory,department,employee,faqs,comment,review,subscribe, blog
from shoppingsite.forms import contactform,signform,commentform,reviewform,faqsform,subscribeform
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.core.serializers import json
from django.db.models import F
# Create your views here.
	
def designview(request):
	best=products.objects.filter(tag='best').order_by('-id')[:8]
	new=products.objects.filter(tag='new').order_by('-id')[:8]
	featured=products.objects.filter(tag='featured').order_by('-id')[:8]
	top=products.objects.filter(tag='top').order_by('-id')[:8]
	stylish=products.objects.filter(tag='stylish').order_by('-id')[:8]
	popular=products.objects.filter(tag='popular').order_by('-id')[:8]
	awesome=products.objects.filter(tag='awesome').order_by('-id')[:8]
	trending=products.objects.filter(tag='trending').order_by('-id')[:8]
	beautiful=products.objects.filter(tag='beautiful').order_by('-id')[:8]
	men=products.objects.filter(genreid_id=1,tag='stylish')
	women=products.objects.filter(genreid_id=2,tag='stylish')
	kids=products.objects.filter(genreid_id=3,tag='stylish')
	context={'best':best,'stylish':stylish,'new':new,'popular':popular,'top':top,'featured':featured,'awesome':awesome,'beautiful':beautiful,'trending':trending,'men':men,'women':women,'kids':kids}
	return render(request,'design1.html',context)
	
def shopproducts(request,id, subid):
	pro=products.objects.select_related('subcatid').get(id=id)
	rpro=products.objects.filter(subcatid_id=subid)
	com=comment.objects.filter(productid_id=id)
	rev=review.objects.filter(pid_id=id)
	cart_product_form = CartAddProductForm()
	context={'pro':pro,'rpro':rpro,'com':com,'cart_product_form': cart_product_form,'rev':rev}
	return render(request,'shopproducts.html',context)

def shopcategory1view(request,id):
	cat=category.objects.all()
	pro=products.objects.filter(genreid_id=id)
	url_parts=request.path.split('/')
	urlgenre=url_parts[2]
	context={'cat':cat,'pro':pro,'urlgenre':urlgenre}
	return render(request,'shopcategory1.html',context)
	
def showproductview(request,id,catid):
	#cat=subcategory.objects.select_related('catid_id').filter(catid_id=catid)
	pro=products.objects.filter(genreid_id=id).filter(subcatid_id__in=subcategory.objects.select_related('catid_id').filter(catid_id=catid))
	context={'pro':pro}
	return render(request,'showproduct.html',context)
	
def categoryproductsview(request,subid):
	rpro=products.objects.filter(subcatid_id=subid)
	context={'rpro':rpro}
	return render(request,'categoryproducts.html',context)
    
def offer(request):
	pro= products.objects.annotate(offer=((F('mrp')-F('sellingprice'))/F('mrp'))*100).filter(offer__gt=50)
	context={'pro':pro}
	return render(request,'offer.html',context)
	   
def viewmore(request,t):
	fea=products.objects.filter(tag=t)
	context={'fea':fea}
	return render(request,'viewmore.html',context)
	   
def searchview(request):
	srh=request.GET['qname']
	pro=products.objects.filter(name__icontains=srh)
	context={'pro':pro}
	return render(request,'search.html',context)

class securityview(TemplateView):
	template_name="security.html"
	
class contactview(TemplateView):
	template_name="contact.html"
	
class aboutsview(TemplateView):
	template_name="abouts.html"
	
class termsconditionsview(TemplateView):
	template_name="termsconditions.html"
	
class returnrefundview(TemplateView):
	template_name="returnrefund.html"
	
class privacypolicyview(TemplateView):
	template_name="privacypolicy.html"
	
class faqsview(ListView):
	template_name="faqs.html"
	def get_queryset(self):
		return faqs.objects.all()
	
def insertcontactform(request):
	if request.method=='POST':
		form=contactform(request.POST,request.FILES)
	if form.is_valid():
		try:
			form.save()
			return redirect('/contact/')
		except:
			pass
	else:
		form=contactform()
		return render(request,'contact.html',{'form':form})
		
def signup(request):
	if request.method=='POST':
		form=signform(request.POST)
		if form.is_valid():
			try:
				user=form.save()
				login(request,user)
				return redirect('/design1/')
			except:
				pass
	else:
		form=signform()
	return render(request,'registration/sign.html',{'form':form})
	
def insertsubscribe(request):
	if request.method=='POST':
		form=subscribeform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/design1/')
			except:
				pass
	else:
		form=subscribeform()
	return render(request,'base.html',{'form':form})

	
def showemp(request):
	dept=department.objects.all()
	context={'dept':dept}
	return render(request,'emp.html',context)
	
def showemployee(request,id):
	emp=employee.objects.filter(depid_id=id)
	context={'emp':emp}
	return render(request,'employee.html',context)
	
	
'''def insertcomment(request):
	if request.method == 'POST':
		form=commentform(request.POST)
		if form.is_valid():
			form.save()
			response_data['result'] = 'Comment post successful!'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)
	else:
		return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
	return render(request,'shopproducts.html',{'form':form})
'''

def insertcomment(request):
	form=commentform(request.POST)
	form.save()
	return render(request,'shopproducts.html',{'form':form})
	
def insertreview(request):
	form=reviewform(request.POST)
	if form.is_valid():
		form.save()
	return render(request,'shopproducts.html',{'form':form})
	
def insertorder(request):
	if request.method=='POST':
		form=orderform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/order/')
			except:
				pass
	
	else:
		form=orderform()
		
	return render(request,'order.html',{'form':form})
    

def blogview(request):
	blogs=blog.objects.all().order_by('-id')
	context={'blogs':blogs}
	return render(request,'blog.html',context)    
    
    
def blogdetailview(request,id):
	blogs=blog.objects.get(id=id)
	context={'blogs':blogs}
	return render(request,'blogdetail.html',context)        