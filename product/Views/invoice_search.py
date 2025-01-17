from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from ..models.products import Product
from ..models.Sales_limca import Sales_limca
from ..models.basket import Basket
from ..models.invoice import Invoice
from ..models.expense import Expense
from .add_to_invoice import Add_to_invoice, delete_sale, plus_quantity, minus_quantity
from django.db.models import Q
from datetime import datetime, timedelta, date
from ..middlewares.auth import login_auth_middleware
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class Invoice_Search(View):

    @method_decorator(login_auth_middleware)    
    def get(self, request): 
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        end_date = request.GET.get('end_date')
        search = request.GET.get('search')
        data = {}
        invoices_total_price = []
        expense_total_price = []

        if search:
            invoices = Invoice.objects.filter(id=int(search))
            invoices_length = len(invoices)
            for n in invoices:
                if n.discounted_amount:
                    invoices_total_price.append(n.discounted_amount)
                else:
                    invoices_total_price.append(n.total_price)
            
            data = {
                'invoices': invoices,
                'length': invoices_length,
                'year':year,
                'month':month,
                'day':day,
                'total_sale':sum(invoices_total_price),
            }
            return render(request, 'invoice_search.html', data)



        
        if year and month and day and not end_date :
            specific_date = date(int(year), int(month), int(day))
            print(specific_date)

            invoices = Invoice.objects.filter(date=specific_date)
            expenses = Expense.objects.filter(date__date=specific_date)
            invoices_length = len(invoices)
            for n in invoices:
                if n.discounted_amount:
                    invoices_total_price.append(n.discounted_amount)
                else:
                    invoices_total_price.append(n.total_price)
            for ex in expenses:
                expense_total_price.append(ex.price)

            data = {
                'invoices': invoices,
                'expenses': sum(expense_total_price),
                'length': invoices_length,
                'year':year,
                'month':month,
                'day':day,
                'total_sale':sum(invoices_total_price),
            }
        
        elif year and month and not day :
            first_day = date(int(year), int(month), 1)
            print(first_day)

            if int(month) == 12:
                last_day = date(int(year) + 1, 1, 1) - timedelta(days=1)
            else:
                last_day = date(int(year), int(month) + 1, 1) - timedelta(days=1)
            print(last_day)

            invoices = Invoice.objects.filter(date__range=(first_day, last_day))
            expenses = Expense.objects.filter(date__date__range=(first_day, last_day))
            invoices_length = len(invoices)
            for n in invoices:
                if n.discounted_amount:
                    invoices_total_price.append(n.discounted_amount)
                else:
                    invoices_total_price.append(n.total_price)
            for ex in expenses:
                expense_total_price.append(ex.price)

            data = {
                'invoices': invoices,
                'expenses': sum(expense_total_price),
                'length': invoices_length,
                'year':year,
                'month':month,
                'day':day,
                'total_sale':sum(invoices_total_price),
            }
        
        elif year and month and day and end_date :
            first_day = datetime(int(year), int(month), int(day))
            last_day = datetime(int(year) , int(month), int(end_date), 23, 59, 59)

            invoices = Invoice.objects.filter(date__range=(first_day.date(), last_day.date()))
            expenses = Expense.objects.filter(date__date__range=(first_day.date(), last_day.date()))
            invoices_length = len(invoices)
            for n in invoices:
                if n.discounted_amount:
                    invoices_total_price.append(n.discounted_amount)
                else:
                    invoices_total_price.append(n.total_price)

            for ex in expenses:
                expense_total_price.append(ex.price)

            data = {
                'invoices': invoices,
                'expenses': sum(expense_total_price),
                'length': invoices_length,
                'year':year,
                'month':month,
                'day':day,
                'end_date':end_date,
                'total_sale':sum(invoices_total_price),
            }
        else:
            invoices = Invoice.objects.all()
            expenses = Expense.objects.all() 
            for n in invoices:
                if n.discounted_amount:
                    invoices_total_price.append(n.discounted_amount)
                else:
                    invoices_total_price.append(n.total_price)
            for ex in expenses:
                expense_total_price.append(ex.price)


            invoices_length = len(invoices)
        # paginator = Paginator(invoices, 20)
        # page_number = request.GET.get('page')
        # request.session['page_number'] = page_number

        # try:
        #     page_obj = paginator.page(page_number)
        # except PageNotAnInteger:
        #     page_obj = paginator.page(1)
        # except EmptyPage:
        #     page_obj = paginator.page(paginator.num_pages)

        
            data = {
                # 'invoices': page_obj,
                'invoices': invoices,
                'expenses': sum(expense_total_price),
                'length': invoices_length,
                'total_sale':sum(invoices_total_price),
            }

        return render(request, 'invoice_search.html', data)