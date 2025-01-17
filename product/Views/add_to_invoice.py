from django.shortcuts import render
from django.views import View
# Create your views here.
from ..models.products import Product
from ..models.customer import Customer
from ..models.basket import Basket
from ..models.invoice import Invoice
from ..models.Sales_limca import Sales_limca


def Add_to_invoice(product_id):
    product = Product.objects.get(id=product_id)
    sales = Basket.objects.all().first() 
    customer = None
    if sales:
        customer = sales.customer 
    else:   
        customer = Customer.objects.create(name='new_customer')

    if customer:
        try:
            check_sale_exist = Basket.objects.filter(customer=customer,product=product)
            if check_sale_exist:
                for sale in check_sale_exist:
                    sale.quantity = sale.quantity+1
                    sale.total_price = product.price*sale.quantity  
                    sale.save()
            else:
                product_price = product.price
                sale_list = Basket.objects.create(customer=customer, quantity=1,product=product,total_price=product_price)
        except Exception as e:
            print(e)

    return 0     

def delete_sale(product_id):
    sale = Basket.objects.get(id=product_id)
    sale.delete()

    return 0

def plus_quantity(sale_id):
    sale = Basket.objects.get(id=sale_id)
    if sale:
        sale.quantity = sale.quantity+1
        sale.total_price = sale.product.price * sale.quantity
        sale.save()
    return 0


def minus_quantity(sale_id):
    sale = Basket.objects.get(id=sale_id)
    if sale:
        if sale.quantity <= 0:
           return 0
        else:
            sale.quantity = sale.quantity-1
            sale.total_price = sale.product.price * sale.quantity
            sale.save()
    
    return 0


def Edit_invoice(invoice_id, product_id):
    customer = None
    if invoice_id:
        print(invoice_id)
        print(product_id)
        get_invoice = Invoice.objects.get(id=invoice_id)
        if get_invoice:
            get_product = Product.objects.get(id=product_id)
            invoice_sales = get_invoice.products.all()
            for p in invoice_sales:
                customer = p.customer
            sale = Sales_limca.objects.create(customer=customer,quantity=1,product=get_product,total_price=get_product.price)
            if sale:
                get_invoice.products.add(sale)
                if get_invoice.discount:
                    decimal_value = get_invoice.discount/100
                    percentage_price = get_product.price * decimal_value
                    after_discount_price = get_product.price - percentage_price 
                    get_invoice.discount = int(get_invoice.discount)
                    get_invoice.discounted_amount = after_discount_price
                    get_invoice.save()
                else:
                    get_invoice.total_price = get_invoice.total_price + get_product.price
                    get_invoice.save()
               
            
        
    return 0

def del_invoice_product(invoice_id, product_id):
    if invoice_id:
        get_invoice = Invoice.objects.get(id=invoice_id)
        if get_invoice:
            if get_invoice:
                get_invoice.products.remove(product_id)
                get_invoice.save()
            
    return 0



