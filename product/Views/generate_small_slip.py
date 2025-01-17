from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..models.Sales_limca import Sales_limca
from ..models.basket import Basket
from ..models.invoice import Invoice
from django.http import HttpResponse
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator




class Small_invoive(View):
    @method_decorator(login_auth_middleware)
    def get(self, request):

        return render(request, 'slip.html')
    @method_decorator(login_auth_middleware)
    def post(self, request):

        basket = Basket.objects.all()
        discount = request.POST.get('discount')
        gross_amount = request.POST.get('gross_amount')
        net_total = request.POST.get('net_total')
        status = request.POST.get('status')
        delivery = request.POST.get('delivery')
        paid_or_not = request.POST.get('paid_or_not')
        recieved_cash = request.POST.get('recieved_cash')
        returned_cash = None  

        make_invoice = []

        print(net_total)
        print(gross_amount)
        print(discount)
        

        if basket:
            for b in basket:
                save_basket_product = Sales_limca.objects.create(customer=b.customer,quantity=b.quantity,product=b.product,total_price=b.total_price)
            
                make_invoice.append(save_basket_product)
           
            
            if recieved_cash and int(discount) == 0:
                returned_cash = int(recieved_cash) - int(gross_amount)
                print(float(recieved_cash) ,float(gross_amount))
                print(float(recieved_cash) - float(gross_amount))

            elif recieved_cash and int(discount) > 0:
                returned_cash = float(recieved_cash) - float(net_total)
                print(float(recieved_cash) ,float(net_total))
                print(float(recieved_cash) - float(net_total))
            else:
                recieved_cash = 0
                returned_cash = 0
            
            
            if delivery and net_total and int(discount) > 0:
                net_total = float(net_total) + float(delivery)
            else:
                gross_amount = float(gross_amount) + float(delivery)


            del_Basket = Basket.objects.all().delete()
            
            if int(discount) == 0 and delivery:
                save_invoice = Invoice.objects.create(total_price= float(gross_amount),discounted_amount=float(net_total),status=status,delivery_charges=delivery,recieved_cash=recieved_cash,returned_cash=returned_cash)
            elif delivery and int(discount) > 0:
                save_invoice = Invoice.objects.create(total_price= float(gross_amount),discounted_amount=float(net_total),discount=discount,status=status,delivery_charges=delivery,recieved_cash=recieved_cash,returned_cash=returned_cash)
            elif int(discount) > 0 and not delivery:
                save_invoice = Invoice.objects.create(total_price= float(gross_amount),discounted_amount=float(net_total),discount=discount,status=status,recieved_cash=recieved_cash,returned_cash=returned_cash)
            else:
                save_invoice = Invoice.objects.create(total_price= float(gross_amount),discounted_amount=float(net_total),status=status,recieved_cash=recieved_cash,returned_cash=returned_cash)
            
          
            if paid_or_not == 'on':
                save_invoice.paid_or_not = True
                save_invoice.save()

            for product in make_invoice:
                save_invoice.products.add(product)
                save_invoice.save()
            
            sale_products = save_invoice.products.all()
            final_invoice = save_invoice
            
           

            data={
                'sale_products':sale_products,
                'invoice': final_invoice,
            }

            return render(request, 'small_slip.html', data)
            
        else:
            return render(request, 'small_slip.html')