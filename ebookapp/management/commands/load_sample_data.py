# myapp/management/commands/load_sample_data.py

import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from ebookapp.models import Category, SubCategory, Book

class Command(BaseCommand):
    help = 'Load sample data from CSV files into the database'

    def handle(self, *args, **kwargs):
        
        self.load_books()


    def load_books(self):
        path = os.path.join(settings.BASE_DIR, 'ebookapp', 'data', 'books.csv')
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = Category.objects.get(id=row['category_id'])
                subcategory = SubCategory.objects.get(id=row['subcategory_id'])
                Book.objects.get_or_create(
                    id=row['id'],
                    title=row['title'],
                    author=row['author'],
                    published_date=row['published_date'],
                    category=category,
                    subcategory=subcategory,
                    description=row['description']  # Added description field
                )
            self.stdout.write(self.style.SUCCESS('Successfully loaded books'))
