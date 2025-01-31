from django.urls import path
from .import views
urlpatterns = [
    path('',views.homepage),
    path('shop',views.shop,name='shop'),
    path('product',views.product,name='product'),
    path('contact',views.contact,name='contact'),
    path('signin',views.signin,name= 'signin'),
    path('contact_data',views.contact_data,name="contact_data"),
    path('save',views.save,name= 'save'),
    path('show',views.show_data,name= 'show'),
    
]