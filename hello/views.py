from django.shortcuts import redirect, render
from hello.db_queries import get_random_two
from django.views.generic.base import View
from django.contrib.auth import login
from django.http import JsonResponse
from django.urls import reverse

from hello.forms import LoginForm, RegisterForm


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
                'weapons': random_weapons
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
                'weapons': weapons
            }
        )

class CartView(View):
    def get(self, request, *args, **kwargs):
        print(request.build_absolute_uri()) #optional
        return render(
            request,
            'cart.html'
        )

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
                        if user.is_admin:
                            return JsonResponse({'success': True, 'redirect_url': reverse('admin')})
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
        from hello.models import CustomUser
        from hello.mail_service import send_mail
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password != confirm_password:
                return JsonResponse({'success': False, 'error': 'Passwords do not match'}, status=400)
            
            try:
                user = CustomUser.objects.create_user(username=email, email=email, password=password)
                login(request, user)
                
                # Отправка письма
                send_mail(
                    email=email,
                    subject='Successful Registration',
                    text=f'Hello, {email}!\n\nYou have successfully registered at SpaceShop.'
                )
                
                return JsonResponse({'success': True, 'redirect_url': reverse('catalog')})
            except Exception as e:
                print("ERROR:", e)
                return JsonResponse({'success': False, 'error': 'An unexpected error occurred'}, status=400)
        else:
            # Возвращаем ошибки формы в JSON
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
