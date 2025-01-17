from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator
from ..models.birthday import Birthday

class BirthdayView(View):
    
    @method_decorator(login_auth_middleware)    
    def get(self, request):

        return render(request, 'birthday.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('birth')
        error_message = None
        if name:
            try:
                birthday = Birthday.objects.create(name=name,phone=phone,date=date)
                error_message = "birthday has been added"
            except Exception as e:
                error_message = f"An error occured: {e}"

        data={
            'error':error_message,
        }

        return render(request, 'birthday.html',data)
