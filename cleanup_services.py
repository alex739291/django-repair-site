
import os
import django
import sys

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import Service
from django.db.models import Q

def cleanup_and_update():
    # Define the canonical data
    services_data = {
        'Lavatrici': {
            'keywords': ['lavatric', 'lavatrice'],
            'title': 'Riparazione Lavatrici', # Standardize title
            'short': "Riparazione professionale di problemi di scarico, cuscinetti e scheda elettronica.",
            'desc': """Se la tua lavatrice non scarica correttamente, emette rumori forti durante la centrifuga o visualizza codici di errore sul display digitale, è fondamentale un intervento tempestivo. I nostri tecnici specializzati a Como sono esperti nella diagnosi di guasti complessi, come l'usura dei cuscinetti del cestello, malfunzionamenti della pompa di scarico o difetti della scheda elettronica di controllo.
Non ignorare i primi segnali: vibrazioni eccessive o perdite d'acqua possono indicare problemi che, se trascurati, portano a danni irreparabili. Garantiamo l'utilizzo esclusivo di ricambi originali certificati, essenziali per ripristinare la silenziosità e l'efficienza energetica del tuo elettrodomestico. Offriamo un servizio rapido per ridurre al minimo il disagio di restare senza lavatrice, assicurando una riparazione duratura e coperta da garanzia."""
        },
        'Frigoriferi': {
            'keywords': ['frigorifer', 'frigo'],
            'title': 'Riparazione Frigoriferi',
            'short': "Intervento rapido su ricariche gas, termostati e sensori No-Frost.",
            'desc': """Un frigorifero che non raffredda adeguatamente o che genera ghiaccio in eccesso rappresenta un rischio per la conservazione dei tuoi alimenti. I nostri tecnici intervengono con urgenza su frigoriferi domestici e combinati, diagnosticando problemi legati alla perdita di gas refrigerante, guasti al compressore o malfunzionamenti del termostato.
Siamo specializzati nei moderni sistemi No-Frost, dove spesso i sensori di temperatura o le ventole di ricircolo possono bloccarsi. Una riparazione tempestiva è cruciale per evitare il deterioramento dei cibi e sprechi costosi. Utilizziamo strumentazione all'avanguardia per individuare micro-perdite nel circuito e sostituire le guarnizioni usurate che compromettono l'isolamento termico. Affidati alla nostra esperienza per ripristinare la temperatura ideale e l'efficienza del tuo frigorifero in tempi rapidi."""
        },
        'Lavastoviglie': {
            'keywords': ['lavastovigli'],
            'title': 'Riparazione Lavastoviglie',
            'short': "Risoluzione ostruzioni, problemi pompa e perdite d'acqua con ricambi originali.",
            'desc': """La tua lavastoviglie non lava bene, lascia residui o perde acqua sul pavimento? Spesso questi problemi sono causati da ostruzioni nei bracci rotanti, filtri intasati o malfunzionamenti della pompa di scarico. Il nostro servizio di assistenza a Como si occupa di ripristinare le prestazioni ottimali del tuo elettrodomestico, intervenendo anche su guasti alla resistenza che impediscono all'acqua di scaldarsi.
Utilizziamo ricambi originali per sostituire pompe, elettrovalvole e guarnizioni danneggiate. Inoltre, offriamo consulenza sull'uso corretto di detergenti e decalcificanti professionali per prevenire l'accumulo di calcare, nemico numero uno delle lavastoviglie. Un intervento professionale non solo risolve il guasto immediato, ma prolunga la vita utile dell'apparecchio, garantendo stoviglie brillanti e igienizzate ad ogni ciclo."""
        },
        'Asciugatrici': {
            'keywords': ['asciugatric'],
            'title': 'Riparazione Asciugatrici',
            'short': "Manutenzione condotti, sostituzione cinghie e prevenzione surriscaldamento.",
            'desc': """L'asciugatrice è indispensabile, specialmente nei mesi invernali. Se noti che i panni restano umidi, i tempi di asciugatura si allungano o l'apparecchio si surriscalda, potrebbe esserci un problema nei sensori di umidità o nel sistema di ventilazione. I nostri tecnici sono qualificati per intervenire su asciugatrici a condensazione e a pompa di calore.
Effettuiamo una pulizia approfondita dei condotti della condensa e dei filtri, spesso causa di blocchi e rischi di surriscaldamento. Sostituiamo cinghie spezzate, tendicinghia rumorosi e schede di controllo difettose. La manutenzione corretta è vitale non solo per l'efficienza energetica, ma anche per la sicurezza domestica. Ripristiniamo il funzionamento perfetto della tua asciugatrice con ricambi garantiti, assicurandoti bucato morbido e asciutto in tempi brevi."""
        }
    }

    for key, data in services_data.items():
        print(f"Processing type: {key}")
        # Find all services matching keywords
        q_objects = Q()
        for kw in data['keywords']:
            q_objects |= Q(title__icontains=kw)
        
        matches = Service.objects.filter(q_objects).order_by('id')
        
        if not matches.exists():
            print(f"  No service found for {key}. Creating new...")
            Service.objects.create(
                title=data['title'],
                slug=key.lower(),
                description=data['desc'],
                short_description=data['short'],
                image='services/placeholder.jpg'
            )
            continue
            
        print(f"  Found {matches.count()} matches: {[s.title for s in matches]}")
        
        # Keep the first one (oldest ID)
        main_service = matches.first()
        print(f"  Updating main service (ID {main_service.id}): {main_service.title}")
        
        main_service.title = data['title'] # Normalize title
        main_service.description = data['desc']
        main_service.short_description = data['short']
        main_service.save()
        
        # Delete duplicates
        for duplicate in matches[1:]:
            print(f"  Deleting duplicate (ID {duplicate.id}): {duplicate.title}")
            duplicate.delete()

    print("Cleanup and update finished.")

if __name__ == '__main__':
    cleanup_and_update()
