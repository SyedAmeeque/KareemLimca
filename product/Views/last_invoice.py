from django.shortcuts import render, redirect
from django.views import View
from ..models.invoice import Invoice
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator

class Last_Invoice(View):
    
    @method_decorator(login_auth_middleware)    
    def get(self, request):
        get_invoice = Invoice.objects.all().last()
        get_sales = get_invoice.products.all()

        data={
            'sale_products':get_sales,
            'invoice':get_invoice,
        }

        return render(request, 'last_invoice.html',data)
