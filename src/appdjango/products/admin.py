from django.contrib import admin

# Register your models here.
from .models import Product #relative import. imports class from models.py. relative because both files are on same directory

admin.site.register(Product)
