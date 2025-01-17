from django.contrib import admin
from .models.category import Category
from .models.customer import Customer
from .models.invoice import Invoice
from .models.products import Product
from .models.basket import Basket
from .models.Sales_limca import Sales_limca
from .models.birthday import Birthday
from .models.expense import Expense

# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display =('name', 'price', 'large_price', 'category')
admin.site.register(Product,productAdmin)

class customerAdmin(admin.ModelAdmin):
    list_display =('name', 'phone')
admin.site.register(Customer,customerAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
admin.site.register(Category,categoryAdmin)


class selled_products_Admin(admin.ModelAdmin):
    list_display =('customer', 'quantity', 'product')
admin.site.register(Basket,selled_products_Admin)

class InvoiceAdmin(admin.ModelAdmin):
    list_display =('id','total_price','discount','date','time')
admin.site.register(Invoice, InvoiceAdmin)

class SalesAdmin(admin.ModelAdmin):
    list_display =('total_price','quantity','date')
admin.site.register(Sales_limca, SalesAdmin)

class birthdayAdmin(admin.ModelAdmin):
    list_display =('name','phone','date')
admin.site.register(Birthday, birthdayAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    list_display =('name','price')
admin.site.register(Expense, ExpenseAdmin)





