from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator
from ..models.birthday import Birthday
from ..models.expense import Expense

class ExpenseView(View):
    
    @method_decorator(login_auth_middleware)    
    def get(self, request):

        return render(request, 'expense.html')

    def post(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        error_message = None
        if name:
            try:
                create_expense = Expense.objects.create(name=name,price=price)
                error_message = "Expense has been added"
            except Exception as e:
                error_message = f"An error occured: {e}"

        data={
            'error':error_message,
        }

        return render(request, 'expense.html',data)
