from django.db import models
import re
from datetime import *


class CustomerManager(models.Manager):
    def register(self.postData):
    # RegEx for email
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    # RegEx for Password
    PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

    FISRT_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

    LAST_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

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

    return errors

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
        if not country_REGEX.match(postData['country']):
            errors['country-invalid'] = 'Invalid country!'
        check = Customer.objects.filter(country=postData['country'].lower())
        if len(check) > 0:
            errors['country-inuse'] = 'country already in use!'


# Validating address
        if len(postData['address']) < 1:
            errors['address'] = 'address is required!'
        if not EMAIL_REGEX.match(postData['address']):
            errors['address-invalid'] = 'Invalid address!'
        check = Customer.objects.filter(address=postData['address'].lower())
        if len(check) > 0:
            errors['address-inuse'] = 'address already in use!'


# Validating postal_code
        if len(postData['postal_code']) < 1:
            errors['postal_code'] = 'postal_code is required!'
        if not postal_code_REGEX.match(postData['postal_code']):
            errors['postal_code-invalid'] = 'Invalid postal_code!'
            check = Customer.objects.filter(postal-code=postData['postal_code'].lower())
        if len(check) > 0:
            errors['postal_code-inuse'] = 'postal_code already in use!'


# Validating phone_number
        if len(postData['phone_number']) < 1:
            errors['phone_number'] = 'phone_number is required!'
        if not EMAIL_REGEX.match(postData['phone_number']):
            errors['phone_number-invalid'] = 'Invalid phone_number!'
        check = Customer.objects.filter(phone_number=postData['phone_number'].lower())
        if len(check) > 0:
            errors['phone_number-inuse'] = 'phone_number already in use!'


# Validating Password
        if len(postData['password']) < 1:
            errors['password'] = 'Password is required!'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 1 number and capitalization!'

        if len(postData['password_confirm']) < 1:
            errors['password_confirm'] = 'Confirm password is required!'
        elif postData['password_confirm'] != postData['password']:
            errors['passwords_match'] = 'Password must match Confirm password!'




class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomerManager()




