from django.db import models
 
class Log_In_ID(models.Model):
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    class Meta:
        db_table = 'login'



class Data(models.Model):
    name = models.CharField(max_length=190)
    mobile = models.IntegerField()
    email = models.CharField(max_length=190)
    address = models.CharField(max_length=190)
    pincode = models.IntegerField()
    idproof = models.CharField(max_length=190)
    idnumber = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    # Idproof = models.CharField(max_length=255)
   
    class Meta:
        db_table = 'booking'


class Food(models.Model):
    name = models.CharField(max_length=190)
    mobile = models.IntegerField()
    time = models.DateField()
    item = models.CharField(max_length=190)
    quantity = models.IntegerField()
    class Meta:
        db_table = 'food'


class Query(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    class Meta:
        db_table = 'Query'


class Invoice(models.Model):
    name = models.CharField(max_length=190)
    address = models.CharField(max_length=190)
    mobile = models.IntegerField()
    email = models.CharField(max_length=190)
    room_price = models.IntegerField()
    room_quantity = models.IntegerField()
    food_price = models.IntegerField()
    food_quantity = models.IntegerField()
    discount = models.IntegerField()
    gst = models.IntegerField()
    total = models.IntegerField()
    # Idproof = models.CharField(max_length=255) 
    class Meta:
        db_table = 'invoice'

