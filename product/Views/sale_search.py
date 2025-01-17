from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from ..models.products import Product
from ..models.Sales_limca import Sales_limca
from ..models.basket import Basket
from ..models.category import Category
from ..models.invoice import Invoice
from .add_to_invoice import Add_to_invoice, delete_sale, plus_quantity, minus_quantity
from django.db.models import Q
from datetime import datetime, timedelta, date
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator


class Sale_Search(View):

    @method_decorator(login_auth_middleware)    
    def get(self, request): 
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        end_date = request.GET.get('end_date')
        search = request.GET.get('search')
        data = {}
       

        if year and month and day and not end_date and not search :
            specific_date = datetime(int(year), int(month), int(day))
            
            sales = Sales_limca.objects.filter(date__date=specific_date)
            sales_length = len(sales) 

            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
                'day':day,
            }    
           
        elif year and month and not day and not search :
            first_day = datetime(int(year), int(month), 1)
            print(first_day)

            # Define the last day of the month
            if int(month) == 12:
                last_day = datetime(int(year) + 1, 1, 1) - timedelta(days=1)
            else:
                last_day = datetime(int(year), int(month) + 1, 1) - timedelta(days=1)
            print(last_day)

            sales = Sales_limca.objects.filter(date__date__range=(first_day, last_day))
            sales_length = len(sales)   
            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
            }
            
           
           
        elif year and month and day and end_date and not search :
            first_day = datetime(int(year), int(month), int(day))
            last_day = datetime(int(year) , int(month), int(end_date), 23, 59, 59)

            sales = Sales_limca.objects.filter(date__date__range=(first_day.date(), last_day.date()))
            sales_length = len(sales)
            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
                'day':day,
                'end_date':end_date,
            }

        elif year and month and day and not end_date and search :
            specific_date = datetime(int(year), int(month), int(day))
            
            sales = Sales_limca.objects.filter(date__date=specific_date)
            sales = sales.filter(product__name__icontains=search)

            sales_length = len(sales) 

            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
                'day':day,
            }    
           
        elif year and month and not day and search :
            first_day = datetime(int(year), int(month), 1)
            print(first_day)

            # Define the last day of the month
            if int(month) == 12:
                last_day = datetime(int(year) + 1, 1, 1) - timedelta(days=1)
            else:
                last_day = datetime(int(year), int(month) + 1, 1) - timedelta(days=1)
            print(last_day)

            sales = Sales_limca.objects.filter(date__date__range=(first_day, last_day))
            sales = sales.filter(product__name__icontains=search)
            sales_length = len(sales)   
            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
            }
            
           
           
        elif year and month and day and end_date and search :
            first_day = datetime(int(year), int(month), int(day))
            last_day = datetime(int(year) , int(month), int(end_date), 23, 59, 59)

            sales = Sales_limca.objects.filter(date__date__range=(first_day.date(), last_day.date()))
            sales = sales.filter(product__name__icontains=search)

            sales_length = len(sales)
            data ={
                'sales': sales,
                'length': sales_length,
                'year':year,
                'month':month,
                'day':day,
                'end_date':end_date,
            }
        

        elif search and not day and not end_date:
            sales = sales.filter(product__name__icontains=search)
            sales_length = len(sales)

            data ={
                'sales': sales,
                'length': sales_length,
            }

           
        else:
            sales = Sales_limca.objects.all()
            sales_length = len(sales)
            data ={
                'sales': sales,
                'length': sales_length,
            }

       

        return render(request, 'sale_search.html', data)