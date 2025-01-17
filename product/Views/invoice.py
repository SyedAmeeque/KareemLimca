from django.shortcuts import render, redirect
from django.views import View
from ..models.invoice import Invoice
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator

class InvoiceView(View):
    
    @method_decorator(login_auth_middleware)    
    def get(self, request, id):
        get_invoice = Invoice.objects.get(id=id)
        get_sales = get_invoice.products.all()

        data={
            'sale_products':get_sales,
            'invoice':get_invoice,
        }

        return render(request, 'invoices.html',data)

    def post(self, request, id):
        paid_or_not =  request.POST.get('paid_or_not')
        recieved_cash = request.POST.get('recieved_cash')
        
        if paid_or_not:
            get_invoice = Invoice.objects.get(id=id)
            get_invoice.paid_or_not = True
            get_invoice.save()
        
        if recieved_cash:
            get_invoice = Invoice.objects.get(id=id)
            
            if recieved_cash and get_invoice.discounted_amount:
                returned_cash = int(recieved_cash) - int(get_invoice.discounted_amount)
                get_invoice.recieved_cash = recieved_cash
                get_invoice.returned_cash = returned_cash
                get_invoice.save()

            elif recieved_cash and not get_invoice.discounted_amount:
                returned_cash = float(recieved_cash) - float(get_invoice.total_price)
                get_invoice.recieved_cash = recieved_cash
                get_invoice.returned_cash = returned_cash
                get_invoice.save()
            else:
                recieved_cash = 0
                returned_cash = 0

            return redirect('invoice', id)
        
        return redirect('invoice', id)


