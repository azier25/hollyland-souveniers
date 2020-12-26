from django.db import models
import re


class CustomerManager(models.Manager):
    def register(self,postData):
        # RegEx for email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # RegEx for Password
        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

        FISRT_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

        LAST_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

        PHONE_REGEX = re.compile(r'^\++[() \- 0-9]{7,}$')

        errors = {}

        # Validating First Name
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        elif not FISRT_NAME_REGEX.match(postData['first_name']):
            errors["first_name"] = "First Name only conatains letter"

        # Validating Last Name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 3 characters"
        elif not FISRT_NAME_REGEX.match(postData['last_name']):
            errors["last_name"] = "Last Name only conatains letter"


# Validating Email
        if len(postData['email']) < 1:
            errors['email'] = 'Email is required!'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email-invalid'] = 'Invalid Email!'
        check = Customer.objects.filter(email=postData['email'].lower())
        if len(check) > 0:
            errors['email-inuse'] = 'Email already in use!'


# Validating country
        if len(postData['country']) < 1:
            errors['country'] = 'country is required!'


# Validating address
        if len(postData['address']) < 1:
            errors['address'] = 'address is required!'


# Validating postal_code
        if len(postData['postal_code']) < 1:
            errors['postal_code'] = 'postal_code is required!'


# Validating phone_number
        if len(postData['phone_number']) < 1:
            errors['phone_number'] = 'phone_number is required!'
        if not PHONE_REGEX.match(postData['phone_number']):
            errors['phone_number-invalid'] = 'Invalid phone_number!'
        check = Customer.objects.filter(phone_number=postData['phone_number'])
        if len(check) > 0:
            errors['phone_number-inuse'] = 'phone_number already in use!'


# Validating Password
        if len(postData['password']) < 1:
            errors['password'] = 'Password is required!'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 1 number and capitalization!'

        if len(postData['confirm_password']) < 1:
            errors['confirm_password'] = 'Confirm password is required!'
        elif postData['confirm_password'] != postData['password']:
            errors['passwords_match'] = 'Password must match Confirm password!'
        
        return errors

    # Login Validation

    def login(self, postData):
        messages = []

        if len(postData['email']) < 1:
            messages.append('Email is required!')

        if len(postData['password']) < 1:
            messages.append('Password is required!')

        return messages




class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomerManager()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=190)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=190)
    image = models.ImageField(upload_to='image')
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name="category",  on_delete=models.CASCADE)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, related_name="customer",  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return  f"{self.quantity} of {self.product.title}"
    
    def get_total_product_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Deliverd','Deliverd'),
        ('in Progress','in Progress'),
        ('Out of order','Out of order')
    )
    status = models.CharField(default = 'Pending',max_length = 255,choices = STATUS)
    total_price = models.FloatField()
    customer_id = models.ForeignKey(Customer, related_name="customer_id",  on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product , related_name="product_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.status} {self.quantity} of {self.product.title}"

    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.price
        return total



