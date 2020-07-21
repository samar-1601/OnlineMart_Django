from django.contrib import admin

# Register your models here.
from . models import Product
# the statement below adds the table 'PRODUCT'
# made by us in shop/models.py to the admin page where
# we can CRUD any data in the table.
admin.site.register(Product)
