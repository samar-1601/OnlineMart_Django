from django.db import models

# Create your models here.
# After creating and saving run the command "python3 manage.py makemigrations" to save these changes in models.py
# And then run the command "python3 manage.py migrate" to finally the apply these changes to the projects
# Now to see whether the changes are applied or not, then see the admin panel
# If admin page is not there, then create a superuser
# by using the command - "python3 manage.py createsuperuser" and enter the username and password
# "Important" --- After making any model you need to register it
# inside the admin.py file of the app

class Product(models.Model):  #Inherits the properties of Model class in models
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subCategory = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='shop/images', default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, default='')
    publish_date = models.DateField()

# Currently, if we try to CRUD in admin, then we will see that product
# details will be stored in something like ProjectObject 1,2...
# which is not good/efficient. So the below code gives the solution
# of this problem. Here, basically we are replacing
# ProjectObject 1,2... by the product name.

    def __str__(self):
        return self.product_name
