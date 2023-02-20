from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
class home(View):
    def get(self, request):
        return render(request, 'base.html')
    
    def post(self, request):
        return render(request, 'base.html')

class loginUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'userAuth/login.html')

    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            return render(request, 'userAuth/login.html', {'error': 'Please fill all fields'})
        
        if not User.objects.filter(email=email).exists():
            return render(request, 'userAuth/login.html', {'error': 'Email does not exist'})
        
        user = auth.authenticate(request, username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'userAuth/login.html', {'error': 'Password is incorrect'})

class registerUser(View):
    def get(self, request):
            if request.user.is_authenticated:
                return redirect('home')
            return render(request, 'userAuth/register.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if not email or not password1 or not password2:
            return render(request, 'userAuth/register.html', {'error': 'Please fill all fields'})
        
        if password1 != password2:
            return render(request, 'userAuth/register.html', {'error': 'Passwords do not match'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'userAuth/register.html', {'error': 'Email already exists'})
        
        try:
            user = User.objects.create_user(username=email, email=email, password=password1)
            user.save()
            return render(request, 'userAuth/login.html', {'success': 'User created successfully'})
        except:
            return render(request, 'userAuth/register.html', {'error': 'Something went wrong'})
        
class logoutUser(View):
    def get(self, request):
        auth.logout(request)
        return render(request, 'base.html', {'success': 'Logout successful'})
