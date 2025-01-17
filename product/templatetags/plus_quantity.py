from django import template
from ..models.Sales_limca import Sales_limca
from ..models.invoice import Invoice
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()



@register.filter(name="get_sales")
def get_quantity(sales):
    
    seen = set()
    unique_objects = []
    for obj in sales:
        name = obj.product.name  # Adjust according to your model structure
        if name not in seen:
            unique_objects.append(obj)
            seen.add(name)
    
                        
    
    return {'sales':unique_objects,'length':len(seen)} 

@register.filter(name="get_data")
def get_data(name, sales):

    get_sale = sales.filter(product__name__exact=name)
    get_quantity = []
    get_date = None
    discount_price_list = []
    final_total = None
    total_price = []
  
  
  
    for sale in get_sale: 
        get_quantity.append(sale.quantity)
        get_date = sale.date
    
        try:           
            if sale.discount_sale is not None:
                price = sale.product.price * sale.quantity
                decimal_value = sale.discount_sale/100
                percentage_price = price * decimal_value
                after_discount_price = price - percentage_price 
                discount_price_list.append(after_discount_price)
            else:
                price = sale.product.price * sale.quantity
                total_price.append(price)
            if total_price and not discount_price_list:
                final_total = sum(total_price)
            elif discount_price_list and not total_price:
                final_total = sum(discount_price_list)
            else:
                final_total = sum(total_price) + sum(discount_price_list) 
        except Exception as e:
           print(e)

       
    
    return {'quantity':sum(get_quantity),'date':get_date,'total_price':final_total} 



