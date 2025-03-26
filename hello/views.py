from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from hello.db_queries import get_random_two
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.urls import reverse

from hello.forms import LoginForm, RegisterForm
from hello.models import CartItem, Weapon


class IndexView(View):
    def get(self, request, *args, **kwargs):
        from hello.baseline_data import init
        from hello.models import Weapon
        weapons_all = Weapon.objects.all()
        if not weapons_all.exists():
            init()
        print(request.build_absolute_uri()) #optional
        random_weapons = get_random_two(weapons_all)
        return render(
            request,
            'index.html',
            {
                'weapons': random_weapons,
                'user': request.user
            }
        )


class AdminView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'admin.html',
            {
                'user': request.user
            }
        )


class CatalogView(View):
    def get(self, request, *args, **kwargs):
        from hello.models import Weapon
        weapons = Weapon.objects.all()
        print(request.build_absolute_uri()) #optional
        print("CATALOG ON")
        return render(
            request,
            'catalog.html',
            {
                'weapons': weapons,
                'user': request.user
            }
        )


class CartView(View):
    def get(self, request, *args, **kwargs):
        # Получаем текущего пользователя
        user = request.user

        # Получаем все записи корзины для текущего пользователя
        cart = CartItem.objects.filter(user=user)  # Здесь мы фильтруем по пользователю
        total = 0
        for item in cart:
            total += item.price()
        print(request.build_absolute_uri())  # optional

        return render(
            request,
            'cart.html',
            {
                'cartitems': cart,  # Передаем записи корзины в контекст
                'user': user,
                'total' : total
            }
        )

    def remove_from_cart(request, item_id):
        if request.method == 'POST':
            # Получаем элемент корзины по item_id
            cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
            cart_item.delete()  # Удаляем элемент из корзины
            return redirect('cart_view')  # Перенаправляем на представление корзин
    
    def add_to_cart(request, weapon_id):
        if request.method == 'POST':
            user = request.user  # Get the current user
            weapon = Weapon.objects.get(id=weapon_id)  # Get the weapon

            # Check if the item is already in the cart
            cart_item, created = CartItem.objects.get_or_create(user=user, weapon=weapon)

            if not created:
                cart_item.quantity += 1  # Increase quantity if item already in cart
            cart_item.save()  # Save the cart item

            return JsonResponse({'success': True, 'message': 'Item added to cart!', 'quantity': cart_item.quantity})

        return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

class ProductView(View):
    def get(self, request, name=None, *args, **kwargs):
        from hello.models import Weapon
        product = Weapon.objects.get(name=name)
        print(request.build_absolute_uri()) #optional
        return render(
            request,
            'product.html',
            {
                'product': product
            }
        )

class LogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'success': True, 'redirect_url': reverse('home')})

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()  # Создайте новую форму для отображения
        return render(request, "index.html", {"form": form})

    def post(self, request):
        from hello.auth_email import EmailBackend
        if request.method == 'POST':
            #if form.is_valid():
                #
            print("a")
            form = LoginForm(request.POST)
           
           
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                print(email, password)
                b = EmailBackend()
                user = b.authenticate(request=request, username = email, password=password)
                print(user)
                if user is not None:
                    try:
                        login(request, user)
                        if user.is_superuser:
                            return JsonResponse({'success': True, 'redirect_url': reverse('admin')})
                        elif user.is_admin:
                            return JsonResponse({'success': True, 'redirect_url': reverse('siteadmin')})
                        else:
                            return JsonResponse({'success': True, 'redirect_url': reverse('catalog')})
                    except Exception as e:
                        print("ERROR:", e)
                        return JsonResponse({'success': False, 'error': str(e)}, status=500)
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)

            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                form = LoginForm()
                return render(request, "index.html", {"form": form})
        
    
class RegisterView(View):
    def post(self, request):
        print("Received POST request with data: %s", request.POST)
        from hello.models import CustomUser
        import web_project.settings
        from django.core.mail import send_mail
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("ERROR!!", form.cleaned_data)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password != confirm_password:
                return JsonResponse({'success': False, 'error': 'Passwords do not match'}, status=400)
            
            try:
                user = CustomUser.objects.create_user(username=name, email=email, password=password)
                login(request, user)
                
                # Отправка письма
                #send_mail("Succesful Registration", "Hello there and welcome! Now you are a user of the Space Shop!", web_project.settings.EMAIL_HOST_USER, [email])
                return JsonResponse({'success': True, 'redirect_url': reverse('catalog')})
            except Exception as e:
                print("ERROR:", e)
                return JsonResponse({'success': False, 'error': 'An unexpected error occurred'}, status=400)
        else:
            # Возвращаем ошибки формы в JSON
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
