from django.contrib import admin

# Register your models here.
from .models import Loan, Customer, Branch
admin.site.register(Loan)
admin.site.register(Branch)
admin.site.register(Customer)
