from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your POS dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
        return render(request, 'login.html')
