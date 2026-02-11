
import os
import django
import sys

# Add the project root to the python path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import Service

def list_services():
    services = Service.objects.all()
    for s in services:
        print(f"ID: {s.id} | Title: {s.title} | Slug: {s.slug}")

if __name__ == '__main__':
    list_services()
