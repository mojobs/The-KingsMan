# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

import random

def r():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)

    f = str(a) + str(b) +str(c) + str(d)

    return int(f)

class Cloth(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=r())
    clothtype = models.CharField(db_column='ClothType', max_length=1)  # Field name made lowercase.
    noofclothes = models.IntegerField(db_column='NoOfClothes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cloth'

    def __str__(self):
        return f'{self.clothtype} - {self.noofclothes} ({self.id})'


class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerId', primary_key=True, max_length=5)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='CustomerAddress', max_length=150)  # Field name made lowercase.
    customernumber = models.CharField(db_column='CustomerNumber', max_length=50)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    customerdate = models.DateField(db_column='CustomerDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return f'{self.customername} ({self.customerid})'


class Delivery(models.Model):
    deliveryid = models.CharField(db_column='DeliveryId', primary_key=True, max_length=5)  # Field name made lowercase.
    deliverydate = models.DateField(db_column='DeliveryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'

    def __str__(self):
        return f'{self.deliverydate} ({self.deliveryid})'


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderId', primary_key=True, max_length=5)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return f'Order {self.orderid} ({self.orderdate})'


class Price(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=r())
    pricetype = models.CharField(db_column='PriceType', max_length=1)  # Field name made lowercase.
    currency = models.DecimalField(db_column='Currency', max_digits=10, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'price'

    def __str__(self):
        return f'Order {self.pricetype} ({self.currency})'
