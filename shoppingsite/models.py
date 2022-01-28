from django.db import models
from django.contrib.auth.models import User

PRODUCT_TAG=(
('new','new'),
('best','best'),
('featured','featured'),
('top','top'),
('popular','popular'),
('stylish','stylish'),
('trending','trending'),
('awesome','awesome'),
('beautiful','beautiful'),
)
AVAILABILITY=(
('In Stock','In Stock'),
('Out of Stock','Out of Stock'),
('Preorder','Preorder')
)

# Create your models here.

class genre(models.Model):
	name=models.CharField(max_length=200)
	pic=models.ImageField(upload_to='products/')
	class Meta:
		db_table="genre"
	def __str__(self):
		return self.name
		
class category(models.Model):
	name=models.CharField(max_length=200)
	pic=models.ImageField(upload_to='products/')
	class Meta:
		db_table="category"
	def __str__(self):
		return self.name
		
class subcategory(models.Model):
	name=models.CharField(max_length=200)
	pic=models.ImageField(upload_to='products/')
	catid=models.ForeignKey(category,on_delete=models.CASCADE, related_name='subcategories')
	class Meta:
		db_table="subcategory"
	def __str__(self):
		return self.name
		
class products(models.Model):
	name=models.CharField(max_length=200)
	brand=models.CharField(max_length=200, default='')
	subcatid=models.ForeignKey(subcategory,on_delete=models.CASCADE,related_name="subcategoryname")
	pic1=models.ImageField(upload_to='products/')
	pic2=models.ImageField(upload_to='products/')
	pic3=models.ImageField(upload_to='products/')
	pic4=models.ImageField(upload_to='products/')
	mrp=models.IntegerField()
	sellingprice=models.IntegerField()
	description=models.CharField(max_length=800)
	specification=models.CharField(max_length=600, default='')
	genreid=models.ForeignKey(genre,on_delete=models.CASCADE)
	tag=models.CharField(max_length=200, choices=PRODUCT_TAG)
	color=models.CharField(max_length=200)
	available=models.CharField(max_length=200, choices=AVAILABILITY)
	class Meta:
		db_table="products"
	def __str__(self):
		return self.brand

class contact(models.Model):
	message=models.CharField(max_length=500)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	sub=models.CharField(max_length=100)	
	class Meta:
		db_table="contacts"

class faqs(models.Model):
	question=models.CharField(max_length=500)
	answer=models.CharField(max_length=1000)
	class Meta:
		db_table="faq"

class comment(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	comment=models.CharField(max_length=1000)
	userid=models.ForeignKey(User,on_delete=models.CASCADE)
	productid=models.ForeignKey(products,on_delete=models.CASCADE,default='')
	class Meta:
		db_table="comment"
		
class review(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	message=models.CharField(max_length=1000)
	userid=models.ForeignKey(User,on_delete=models.CASCADE)
	pid=models.ForeignKey(products,on_delete=models.CASCADE,default='')
	class Meta:
		db_table="review"
		
class subscribe(models.Model):
	email=models.CharField(max_length=500)
	class Meta:
		db_table="subscribe"
		
class department(models.Model):
	name=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	class Meta:
		db_table='department'
	def __str__(self):
		return self.name

class employee(models.Model):
	name=models.CharField(max_length=150)
	salary=models.FloatField()
	depid=models.ForeignKey(department,on_delete=models.CASCADE, related_name='employees')
	class Meta:
		db_table='employee'
	def __str__(self):
		return self.name
        
class blog(models.Model):
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=6000)
    pic=models.ImageField(upload_to='blog/')
    cdate=models.DateField(auto_now=True)
    class Meta:
        db_table='blog'
    def __str__(self):
        return self.title