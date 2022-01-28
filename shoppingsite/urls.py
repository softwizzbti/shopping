from django.urls import path,include
from shoppingsite import views
from django.contrib.auth import views as auth_views

app_name= 'shoppingsite'

urlpatterns = [
	path('design1/', views.designview),
	path('shopcategory1/<int:id>', views.shopcategory1view),
    path('shopproducts/<int:id>/<int:subid>', views.shopproducts),
	path('insertcontactform/', views.insertcontactform),
	path('contact/', views.contactview.as_view()),
	path('faqs/', views.faqsview.as_view()),
	path('emp/', views.showemp),
	path('viewemp/<int:id>', views.showemployee),
	path('login/',auth_views.LoginView.as_view(),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('sign/',views.signup),
	path('insertcomment/', views.insertcomment),
	path('insertreview/', views.insertreview),
	path('termsconditions/', views.termsconditionsview.as_view()),
	path('privacypolicy/', views.privacypolicyview.as_view()),
	path('returnrefund/', views.returnrefundview.as_view()),
	path('about/', views.aboutsview.as_view()),
	path('security/', views.securityview.as_view()),
	path('search/', views.searchview, name='search_result'),
	path('insertsubscribe/', views.insertsubscribe),
	path('showproduct/<int:id>/<int:catid>', views.showproductview),
	path('categoryproducts/<int:subid>', views.categoryproductsview),
	path('offer/',views.offer),
	path('viewmore/<str:t>',views.viewmore),
    path('blog/',views.blogview),
    path('blogdetail/<int:id>',views.blogdetailview),
]