from django.db import models

# Create your models here.
class People(models.Model):
    Username = models.CharField(max_length=50)
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField()
    Joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Fullname

#N:B One person can have only many addresses for convenience and easy tracking
class Address(models.Model):
    Home_address = models.CharField(max_length=200)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Address_owner = models.ForeignKey(People, on_delete=models.CASCADE)

#N:B One person can have many medical expertise field and also work in different hospitals
class Doctor(models.Model):
    Hospital_name = models.CharField(max_length=500)
    Expertise_field = models.CharField(max_length=200)
    Work_email = models.EmailField(max_length=200)
    Salary_in_words = models.CharField(max_length=50)
    Doctor_info = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return self.Hospital_name

#N:B One person can only have one bio
class Bio(models.Model):
    About_you = models.TextField(null=True)
    Bio_ownwer = models.OneToOneField(People, on_delete=models.CASCADE)


class Product(models.Model):
    Product_name = models.CharField(max_length=200)
    Product_description = models.TextField(null=True)
    Product_price_in_dollars = models.DecimalField(max_digits=19, decimal_places=2)

