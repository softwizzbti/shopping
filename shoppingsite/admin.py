from django.contrib import admin
from shoppingsite.models import contact,genre,category,subcategory,products,employee,department,faqs,comment,review, blog
# Register your models here.

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
	list_display=('message','name','email','sub')
	
@admin.register(faqs)
class faqsAdmin(admin.ModelAdmin):
	pass

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
	list_display=('name','email','phone','comment','userid',)
	
@admin.register(review)
class reviewAdmin(admin.ModelAdmin):
	list_display=('name','email','phone','message','userid',)
	
@admin.register(genre)
class genreAdmin(admin.ModelAdmin):
	pass
	
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
	pass
	
@admin.register(subcategory)
class subcategoryAdmin(admin.ModelAdmin):
	pass
	
@admin.register(products)
class productsAdmin(admin.ModelAdmin):
	pass
	
@admin.register(department)
class departmentAdmin(admin.ModelAdmin):
	pass
	
@admin.register(employee)
class employeeAdmin(admin.ModelAdmin):
	pass
    
@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass