from django.urls import path
from . import views

urlpatterns = [
    path('', views.Z_homepage, name='Z_homepage'),
    path('Z_cart', views.Z_cart, name='Z_cart'),
    path('Z_signup', views.Z_signup, name='Z_signup'),
    path('Z_login', views.Z_login, name='Z_login'),
    path('Z_logout', views.Z_logout, name='Z_logout'),



    path('Z_product', views.Z_product, name='Z_product'),
    path('Z_productdetail', views.Z_productdetail, name='Z_productdetail'),

    path('Z_products_category1', views.Z_products_category1, name='Z_products_category1'),
    path('Z_products_category2', views.Z_products_category2, name='Z_products_category2'),
    path('Z_products_category3', views.Z_products_category3, name='Z_products_category3'),
    
    path('Z_signup', views.Z_signup, name='Z_signup'),
    path('Z_admin_dashboard', views.Z_admin_dashboard, name='Z_admin_dashboard'),
    path('Z_add_category', views.Z_add_category, name='Z_add_category'),  
    path('Z_add_products', views.Z_add_products, name='Z_add_products'),  
    path('Z_show_products', views.Z_show_products, name='Z_show_products'),
    path('Z_delete_product/<int:product_id>/', views.Z_delete_product, name='Z_delete_product'),
    path('Z_user_homepage', views.Z_user_homepage, name='Z_user_homepage'),
    path('Z_view_users', views.Z_view_users, name='Z_view_users'),

    path('Z_delete_user/<int:id>/', views.Z_delete_user, name='Z_delete_user'),
    path('category/<int:category_id>/', views.Z_products_category, name='Z_products_category'),

    
    path('Z_add_cart/<int:product_id>/', views.Z_add_cart, name='Z_add_cart'),

    path('Z_checkout', views.Z_checkout, name='Z_checkout'),

    path('delete_cart_item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('increase/<int:k>/', views.increase, name='increase'),
    path('decrease/<int:k>/', views.decrease, name='decrease'),
    

]