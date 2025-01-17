from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator

class Dashboard(View):
    
    @method_decorator(login_auth_middleware)    
    def get(self, request):
        return render(request, 'dashboard.html')

  