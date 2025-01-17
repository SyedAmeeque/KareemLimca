"""
URL configuration for kareem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .Views.home import Home
from .Views.generate_slip import Slip
from .Views.sale_search import Sale_Search
from .Views.last_invoice import Last_Invoice
from .Views.login import Login
from .Views.dashboard import Dashboard
from .Views.invoice_search import Invoice_Search
from .Views.invoice import InvoiceView
from .Views.edit_invoice import edit_Invoice
from .Views.birthday import BirthdayView
from .Views.expense import ExpenseView
from .Views.small_slip import Small_Slip
from .Views.generate_small_slip import Small_invoive



urlpatterns = [
    path('', Dashboard.as_view(), name="dashboard"),
    path('order/', Home.as_view(), name="home"),
    path('generate_slip/', Slip.as_view(), name="slip"),
    path('generate/small_slip/', Small_Slip.as_view(), name="small_slip"),
    path('Sales/', Sale_Search.as_view(), name="sales"),
    path('birthday/', BirthdayView.as_view(), name="birthday"),
    path('expenses/', ExpenseView.as_view(), name="expense"),
    path('last_invoice/', Last_Invoice.as_view(), name="last_invoice"),
    path('invoice/<int:id>/', InvoiceView.as_view(), name="invoice"),
    path('Edit_invoice/<int:id>/', edit_Invoice.as_view(), name="edit_invoice"),
    path('search_invoice/', Invoice_Search.as_view(), name="search_invoice"),
    path('generate_small_invoice/', Small_invoive.as_view(), name="small_invoice"),
    path('login/', Login.as_view(), name="login"),
    
]