import os
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import City, Service

def populate():
    como_towns = [
        "Brunate", "San Fermo della Battaglia", "Lipomo", "Cernobbio", "Blevio", 
        "Tavernerio", "Maslianico", "Montano Lucino", "Cantù", "Fino Mornasco", 
        "Olgiate Comasco", "Erba", "Lurate Caccivio", "Appiano Gentile", "Mariano Comense"
    ]

    varese_towns = [
        "Casciago", "Induno Olona", "Malnate", "Gazzada Schianno", "Lozza", 
        "Azzate", "Buguggiate", "Gavirate", "Arcisate", "Vedano Olona", 
        "Castiglione Olona", "Tradate", "Gallarate", "Busto Arsizio", "Saronno"
    ]

    all_towns = como_towns + varese_towns

    created_cities = []
    
    print("Starting database population...")
    for town_name in all_towns:
        slug = slugify(town_name)
        description = f"Assistenza e riparazione elettrodomestici a {town_name}. Interventi rapidi a domicilio per lavatrici, lavastoviglie, frigoriferi e forni. Tecnici specializzati e qualificati."
        
        city, created = City.objects.get_or_create(
            name=town_name,
            defaults={
                'slug': slug,
                'description': description
            }
        )
        
        if created:
            print(f"[+] Created city: {town_name}")
        else:
            print(f"[*] City already exists: {town_name}")
            
        created_cities.append(city)

    # Link services to the newly created/fetched cities
    services = Service.objects.all()
    if not services:
        print("Warning: No services found in the database. Ensure services exist to link cities.")
    else:
        for service in services:
            service.cities.add(*created_cities)
            print(f"[i] Linked {len(created_cities)} towns to service: '{service.title}'")

    print("Database population completed successfully!")

if __name__ == '__main__':
    populate()
