
import os
import django
import sys

# Add the project root to the python path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import Service

def update_content():
    services_data = {
        'Lavatrici': {
            'short': "Riparazione schede elettroniche, sostituzione cuscinetti rumorosi e pulizia filtri pompa.",
            'desc': """Il nostro servizio di riparazione lavatrici a Como è specializzato nella risoluzione di guasti complessi che bloccano il tuo elettrodomestico. Interveniamo con precisione su schede elettroniche difettose che causano errori di programmazione o mancato avvio del ciclo. Se la tua lavatrice è rumorosa durante la centrifuga, è probabile che i cuscinetti siano usurati: provvediamo alla loro sostituzione utilizzando ricambi di alta qualità per garantire silenziosità e stabilità.
Inoltre, eseguiamo la pulizia profonda e la disostruzione dei filtri della pompa di scarico, spesso causa di blocchi d'acqua e cattivi odori. I nostri tecnici verificano anche lo stato delle guarnizioni dell'oblò e dei tubi di carico/scarico per prevenire allagamenti. Affidati alla nostra competenza per riportare la tua lavatrice alla massima efficienza operativa."""
        },
        'Frigoriferi': {
            'short': "Ricarica gas refrigerante, sostituzione termostati e risoluzione problemi di sbrinamento (No-Frost).",
            'desc': """Garantiamo interventi rapidi per frigoriferi che non raffreddano o che presentano anomalie di temperatura. I nostri tecnici sono equipaggiati per effettuare ricariche di gas refrigerante in sicurezza, individuando e sigillando eventuali micro-perdite nel circuito. Sostituiamo termostati guasti che compromettono la conservazione dei cibi e ripariamo compressori rumorosi o inefficienti.
Per i modelli No-Frost, siamo esperti nella risoluzione di problemi al sistema di sbrinamento automatico: sostituiamo resistenze bruciate, sensori difettosi e ventole bloccate che causano accumulo di ghiaccio. Un intervento professionale non solo salva i tuoi alimenti, ma ottimizza i consumi energetici del tuo frigorifero, prolungandone la vita utile."""
        },
        'Lavastoviglie': {
            'short': "Risoluzione perdite d'acqua, pulizia bracci irroratori e riparazione pompe di lavaggio.",
            'desc': """Se la tua lavastoviglie perde acqua o non lava bene, il nostro team è pronto a intervenire. Ci occupiamo della sostituzione di guarnizioni usurate e manicotti che causano perdite sul pavimento. Effettuiamo la pulizia accurata dei bracci irroratori ostruiti dal calcare, assicurando che l'acqua raggiunga ogni angolo del cestello per stoviglie brillanti.
Ripariamo o sostituiamo pompe di lavaggio e di scarico malfunzionanti, risolvendo problemi di ristagno d'acqua o rumori anomali. Controlliamo anche l'efficienza della resistenza e del sistema di dosaggio del detersivo. Con i nostri ricambi originali e la nostra esperienza, la tua lavastoviglie tornerà come nuova, garantendo igiene e prestazioni eccellenti."""
        },
        'Asciugatrici': {
            'short': "Sostituzione cinghie, pulizia condotti condensa e riparazione sensori di umidità.",
            'desc': """Un'asciugatrice che non asciuga o che si ferma prima del tempo richiede un'analisi tecnica approfondita. Sostituiamo cinghie di trasmissione spezzate o allentate che impediscono al cestello di girare correttamente. Eseguiamo la pulizia completa dei condotti della condensa e dello scambiatore di calore, rimuovendo lanugine e residui che possono causare surriscaldamenti pericolosi e blocchi del sistema.
Calibriamo e sostituiamo i sensori di umidità difettosi per garantire cicli di asciugatura precisi, evitando sprechi di energia e danni ai tessuti. Interveniamo su asciugatrici a condensazione e a pompa di calore di tutte le marche, ripristinando la perfetta funzionalità del tuo elettrodomestico in tempi brevi."""
        }
    }

    print("Inizio aggiornamento contenuti servizi...")

    for title, data in services_data.items():
        # Case insensitive search
        service = Service.objects.filter(title__icontains=title).first()
        if service:
            print(f"Aggiornamento: {service.title}")
            service.description = data['desc']
            service.short_description = data['short']
            service.save()
        else:
            print(f"ATTENZIONE: Servizio non trovato per '{title}'.")

    print("Contenuti aggiornati con successo!")

if __name__ == '__main__':
    update_content()
