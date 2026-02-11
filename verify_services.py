
import os
import django
import sys

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import Service

def list_services():
    services = Service.objects.all().order_by('id')
    print("-" * 50)
    for s in services:
        print(f"ID: {s.id}")
        print(f"Title: {s.title}")
        print(f"Slug: {s.slug}")
        print("-" * 50)

if __name__ == '__main__':
    list_services()
