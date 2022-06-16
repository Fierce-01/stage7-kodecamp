from .models import Product

#1. Insert a new record into the product model
#Listing the product info
Product_info = Product(
    Product_name = "Hp Laptop",
    Product_description = "A neatly used Hp laptop with a 16gb ram and 1tb rom.",
    Product_price_in_dollars = 500.00
)
#Note that the above would not save, to save;
Product_info.save()
#This would save the product info in the product model on our database


#2. Get all the records in the Product table
#To get all record, enter;
Product.objects.all()


#3. Filter Products by their name
#To filter Hp Laptops available;
Product.objects.filter(Product_name = "Hp Laptop")


#4. Get a single record from the Product table
#To get a single record, we can filter in 3 ways;
#First way is to filter the first record,i.e;
Product.objects.filter(Product_name = "Hp Laptop").first()
#Second way is to filter the last record,i.e;
Product.objects.filter(Product_name = "Hp Laptop").last()
#Third way is to filter out a specific record,i.e;
Product.objects.filter(Product_name = "Hp Laptop").filter(Product_description = "A neatly used Hp laptop with a 16gb ram and 1tb rom.").filter(Product_price_in_dollars = 500.00)
#Note that it is possible to get two or more records from the last method, but it is very unlikely.


#5. Change a product price
#Assign a variable to a single record,i.e;
x = Product.objects.filter(Product_name = "Hp Laptop").last()
#Change the product price
x.Product_price_in_dollars = 800.00
#Make sure to save the changes,i.e;
x.save()
#To verify, enter;
x.Product_price_in_dollars
