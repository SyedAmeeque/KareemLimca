from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from ..models.products import Product
from ..models.invoice import Invoice
from ..models.basket import Basket
from ..models.Sales_limca import Sales_limca
from .add_to_invoice import Add_to_invoice, delete_sale, plus_quantity, minus_quantity,del_invoice_product,Edit_invoice
from django.db.models import Q
from django.utils.decorators import method_decorator
from ..middlewares.auth import login_auth_middleware


class edit_Invoice(View):
    
    @method_decorator(login_auth_middleware)
    def get(self, request, id):
        products = Product.objects.all().exclude(name__icontains="large")
        large_products = Product.objects.filter(name__icontains="large")
        get_invoice = Invoice.objects.get(id=id)
        price_list = []
        discount = request.GET.get('discount')
        del_discount = request.GET.get('del_discount')
        total_price = 0
        after_discount_price = 0
        invoice_products = get_invoice.products.all()
        search = request.GET.get('search')
        category = request.GET.get('category_id')
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

        for item in invoice_products:
            print(item)
            price = item.product.price * item.quantity
            price_list.append(price)  
    

        total_price = sum(price_list)

        if discount:
            decimal_value = int(discount)/100
            percentage_price = total_price * decimal_value
            after_discount_price = total_price - percentage_price 
            get_invoice.discount = int(discount)
            get_invoice.discounted_amount = after_discount_price
            get_invoice.save()
            

             
      

        if del_discount:
            discount = 0
            after_discount_price = 0
            get_invoice.discounted_amount = 0
            get_invoice.discount = 0
            get_invoice.save()

        data={
            'products':products,
            'large_products':large_products,
            'total_price':total_price,
            'discount':discount,
            'invoice':get_invoice,
            'invoice_products':invoice_products,
            'discounted_price':after_discount_price,
        } 
        
        return render(request, 'edit_invoice.html', data)
    
    @method_decorator(login_auth_middleware)
    def post(self, request, id):
        plus = request.POST.get('plus')
        minus = request.POST.get('minus')
        invoice_id = id
        
        if plus:
            get_invoice = Invoice.objects.get(id=id)
            if get_invoice:
                get_invoice_sales = get_invoice.products.all()
                get_product = get_invoice_sales.get(product__id=plus)
                if get_product:
                    get_product.quantity = get_product.quantity+1
                    get_product.total_price = get_product.product.price * get_product.quantity
                    get_product.save()
                    get_price = get_product.product.price
                    if get_invoice.discount:
                        decimal_value = get_invoice.discount/100
                        percentage_price = get_price * decimal_value
                        after_discount_price = get_price - percentage_price 
                        get_invoice.discount = int(get_invoice.discount)
                        get_invoice.discounted_amount = after_discount_price
                        get_invoice.save()
                    else:
                        get_invoice.total_price = get_invoice.total_price + get_price
                        get_invoice.save()

            return redirect('edit_invoice', invoice_id)
        if minus:
            get_invoice = Invoice.objects.get(id=id)
            if get_invoice:
                get_invoice_sales = get_invoice.products.all()
                get_product = get_invoice_sales.get(product__id=minus)
                if get_product:
                    get_product.quantity = get_product.quantity-1
                    get_product.total_price = get_product.product.price * get_product.quantity
                    get_product.save()
                    get_price = get_product.product.price
                    if get_invoice.discount:
                        decimal_value = get_invoice.discount/100
                        percentage_price = get_price * decimal_value
                        after_discount_price = get_price - percentage_price 
                        get_invoice.discount = int(get_invoice.discount)
                        get_invoice.discounted_amount = after_discount_price
                        get_invoice.save()
                    else:
                        get_invoice.total_price = get_invoice.total_price + get_price
                        get_invoice.save()
            return redirect('edit_invoice', invoice_id)
          
        product_id = request.POST.get('product_id')
        if product_id:
            try:
                Edit_invoice(invoice_id, product_id)
                return redirect('edit_invoice')
            except Exception as e:
                print(e)
        delete_id = request.POST.get('del_sale_id')
       
        if delete_id:
            del_invoice_product(invoice_id, delete_id)
            return redirect('edit_invoice', invoice_id)
        

        return redirect('edit_invoice', invoice_id)
        