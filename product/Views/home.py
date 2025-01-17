from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from ..models.products import Product
from ..models.invoice import Invoice
from ..models.category import Category
from ..models.basket import Basket
from .add_to_invoice import Add_to_invoice, delete_sale, plus_quantity, minus_quantity
from django.db.models import Q
from django.utils.decorators import method_decorator
from ..middlewares.auth import login_auth_middleware


class Home(View):

    
    
    @method_decorator(login_auth_middleware)
    def get(self, request):
        invoices = Invoice.objects.filter(paid_or_not=False)
        products = Product.objects.all().exclude(name__icontains="large")
        large_products = Product.objects.filter(name__icontains="large")
        sale_products = Basket.objects.all()
        price_list = []
        discount = request.GET.get('discount')
        del_discount = request.GET.get('del_discount')
        search = request.GET.get('search')
        category = request.GET.get('category_id')
        total_price = 0
        after_discount_price = 0
        session_del = request.GET.get('session_del')
        
        if session_del and request.session.get('search') :
           del request.session['search']
           return redirect('home')
        elif session_del and request.session.get('category'):
           del request.session['category']
           return redirect('home')
           
    


        if search:
            request.session['search'] = search
            print(request.session.get('search'))
        
        if category:
            request.session['category'] = int(category)
            print(request.session.get('category'))
     
        


        
        if request.session.get('search'):
            search = request.session.get('search')
            products = products.filter(Q(name__icontains=search)|Q(category__name__icontains=search))
            large_products = large_products.filter(Q(name__icontains=search)|Q(category__name__icontains=search))
        
        if request.session.get('category'):
            category_id = request.session.get('category')
            products = products.filter(category__id=category_id)
            large_products = large_products.filter(category__id=category_id)

        for price in sale_products:
            price_list.append(price.total_price) 


        total_price = sum(price_list)    
        if discount:
            decimal_value = int(discount)/100
            percentage_price = total_price * decimal_value
            after_discount_price = total_price - percentage_price 
            

     
        if del_discount:
            discount = 0
            after_discount_price = 0
        


        data={
            'products':products,
            'large_products':large_products,
            'sale':sale_products,
            'total_price':total_price,
            'discount':discount,
            'invoices':invoices,
            'discounted_price':after_discount_price,
        } 
        
        return render(request, 'index.html', data)
    
    @method_decorator(login_auth_middleware)
    def post(self, request):
        plus = request.POST.get('plus')
        minus = request.POST.get('minus')
        invoice_id = request.POST.get('invoice_id')
        invoice_del_id = request.POST.get('invoice_del_id')
        invoice_get_id = request.POST.get('invoice_get_id')

        
       
        if invoice_id:
            get_invoice = Invoice.objects.get(id=invoice_id)
            get_invoice.paid_or_not = True
            get_invoice.save()
            return redirect('home')
        
        if invoice_del_id:
            get_invoice = Invoice.objects.get(id=invoice_del_id)
            get_invoice.delete()
            return redirect('home')
        
        if invoice_get_id:
            return redirect('invoice',invoice_get_id)

        if plus:
            plus_quantity(plus)
            return redirect('home')
        if minus:
            minus_quantity(minus)
            return redirect('home')
        product_id = request.POST.get('product_id')
        if product_id:
            try:
                Add_to_invoice(product_id)
                return redirect('home')
            except Exception as e:
                print(e)
        delete_id = request.POST.get('del_sale_id')
        if delete_id:
            delete_sale(delete_id)


            return redirect('home')
        return redirect('home')
        