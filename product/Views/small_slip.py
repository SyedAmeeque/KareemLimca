from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models.Sales_limca import Sales_limca
from ..models.basket import Basket
from ..models.invoice import Invoice
from django.http import HttpResponse
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator




class Small_Slip(View):

    @method_decorator(login_auth_middleware)
    def get(self, request):

        return render(request, 'small_slip.html')
    @method_decorator(login_auth_middleware)
    def post(self, request):
        ids_list= []
        checked_invoices = request.POST.get('all_checked_ids')
        invoice_id = request.POST.get('invoice_id')

       

        if invoice_id and checked_invoices:
            try:
                split_values = checked_invoices.split(',')
                for value in split_values:
                    int_value = int(value)
                    ids_list.append(int_value)
                get_invoice = Invoice.objects.get(id = invoice_id)
                if get_invoice:
                    get_invoice_products = get_invoice.products.all()
                    filter_new_ones = get_invoice_products.filter(id__in=ids_list)
                    print(filter_new_ones)

                    data={'sale_products':filter_new_ones,'invoice':get_invoice}
                    return render(request, 'small_slip.html', data)
            except Exception as e:
                print(e)
                return redirect('edit_invoice', invoice_id)
        else:
            return redirect('edit_invoice', invoice_id)
           
               
       