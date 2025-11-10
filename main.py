############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

from db.models import Product  # ensure we’re using the Product model

# --------------------------------------------------------------
# STEP 1: Populate database with sample products
# --------------------------------------------------------------
if not Product.objects.exists():
    Product.objects.create(upc='123456789012', name='Apple', price=0.99)
    Product.objects.create(upc='987654321098', name='Banana', price=0.59)
    Product.objects.create(upc='555555555555', name='Milk', price=3.49)
    print("Database seeded with sample products.")
else:
    print("Database already has products.")

# --------------------------------------------------------------
# STEP 2: Scan product by UPC and show name + price
# --------------------------------------------------------------
while True:
    upc_input = input("\nScan or enter a product UPC (or type 'exit'): ").strip()
    if upc_input.lower() == 'exit':
        break

    try:
        product = Product.objects.get(upc=upc_input)
        print(f"Product: {product.name} | Price: ${product.price}")
    except Product.DoesNotExist:
        print("Unknown product. Please try again.")

