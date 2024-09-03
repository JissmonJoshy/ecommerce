from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages,auth
from .models import Category,Product,userdetail,Cart

from django.contrib.auth.decorators import login_required
# Create your views here.
def Z_homepage(request):
    return render(request,'Z_homepage.html')



@login_required(login_url='Z_homepage')
def Z_user_homepage(request):
    categories = Category.objects.all()  
    return render(request, 'Z_user_homepage.html', {'categories': categories, 'user': request.user})






def Z_product(request):
    return render(request,'Z_product.html')

def Z_productdetail(request):
    return render(request,'Z_productdetail.html')




def Z_products_category1(request):
    return render(request,'Z_products_category1.html')
                                                                        #just images 
def Z_products_category2(request):
    return render(request,'Z_products_category2.html')

def Z_products_category3(request):
    return render(request,'Z_products_category3.html')



def Z_signup(request):
    return render(request,'Z_signup.html')

def Z_admin_dashboard(request):
    return render(request,'Z_admin_dashboard.html')






def Z_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('Z_admin_dashboard')
            else:
                login(request,user)
                return redirect('Z_user_homepage')
        else:
            messages.info(request, 'Invalid username & password')
            return redirect('Z_login')
    return render(request,'Z_login.html')



@login_required(login_url='Z_homepage')
def Z_admin_dashboard(request):
    return render(request, 'Z_admin_dashboard.html')



@login_required(login_url='Z_homepage')
def Z_add_category(request):
    if request.method=="POST":
        Cat_name=request.POST['categoryName']
        Category.objects.create(Category_name=Cat_name)
        return redirect('Z_add_category')
    return render(request,'Z_add_category.html') 




@login_required(login_url='Z_homepage')
def Z_add_products(request):
    categories = Category.objects.all() 
    if request.method == "POST":
        product_name = request.POST['productName']
        description = request.POST['description']
        price = request.POST['price']
        category_id = request.POST['category']
        category = Category.objects.get(id=category_id)
        image = request.FILES['image']
        
        
        Product.objects.create(
            prname=product_name,
            prdesc=description,
            prprice=price,
            category=category,
            primg=image
        )
        return redirect('Z_add_products')
    return render(request, 'Z_add_products.html', {'categories': categories})



@login_required(login_url='Z_homepage')
def Z_show_products(request):
    products = Product.objects.all()  
    return render(request, 'Z_show_products.html', {'products': products})



@login_required(login_url='Z_homepage')
def Z_delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('Z_show_products')



def Z_signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        address = request.POST['address']
        contact_number = request.POST['contact_number']
        image = request.FILES.get('image')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username already exists")
                return redirect('Z_signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email,
                )

                user_details = userdetail(
                    user=user,
                    address=address,
                    number=contact_number,
                    usimg=image
                )
                user_details.save()
                return redirect('Z_homepage')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('Z_signup')
    else:
        return render(request, 'Z_signup.html')

                







@login_required(login_url='Z_homepage')
def Z_view_users(request):
    users=userdetail.objects.all()
    return render(request,'Z_view_users.html',{'users':users})

@login_required(login_url='Z_homepage')
def Z_delete_user(request, id):
    user_details = userdetail.objects.filter(id=id).first()
    
    if user_details:
        user = user_details.user
        user_details.delete()
        
        if user:
            user.delete()
        messages.success(request, "User deleted successfully")
    else:
        messages.error(request, "User does not exist")
    
    return redirect('Z_view_users')





@login_required(login_url='Z_homepage')                         
def Z_logout(request):                        
    auth.logout(request)
    return redirect('Z_homepage')





@login_required(login_url='Z_homepage')
def Z_add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, prod=product)

    if not created:
        
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('Z_cart')





@login_required(login_url='Z_homepage')
def delete_cart_item(request, item_id):
    item = Cart.objects.get(id=item_id)
    item.delete()
    return redirect('Z_cart')

def increase(request,k):
    cart_item=Cart.objects.get(prod_id=k,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('Z_cart')

def decrease(request,k):
    cart_item=Cart.objects.get(prod_id=k,user=request.user)
    cart_item.quantity -=1
    cart_item.save()
    return redirect('Z_cart')



def Z_products_category(request, category_id):
    category = Category.objects.get( id=category_id)
    products = Product.objects.filter(category=category)
    cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'Z_products_category.html', {'category': category, 'products': products, 'cart_count': cart_count})



@login_required(login_url='Z_homepage')
def Z_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    cart_count = cart_items.count()
    return render(request, 'Z_cart.html', {'cart_items': cart_items, 'total': total, 'cart_count': cart_count})



@login_required(login_url='Z_homepage')
def Z_checkout(request):
    cart_count = Cart.objects.filter(user=request.user).count()
    return render(request, 'Z_checkout.html', {'cart_count': cart_count})
