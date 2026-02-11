
import os
import django
import sys

# Add the project root to the python path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')
django.setup()

from pages.models import Service

def update_services():
    services_data = {
        'Lavatrici': {
            'short': "Riparazione professionale di problemi di scarico, cuscinetti e scheda elettronica.",
            'desc': """Se la tua lavatrice non scarica correttamente, emette rumori forti durante la centrifuga o visualizza codici di errore sul display digitale, è fondamentale un intervento tempestivo. I nostri tecnici specializzati a Como sono esperti nella diagnosi di guasti complessi, come l'usura dei cuscinetti del cestello, malfunzionamenti della pompa di scarico o difetti della scheda elettronica di controllo.
Non ignorare i primi segnali: vibrazioni eccessive o perdite d'acqua possono indicare problemi che, se trascurati, portano a danni irreparabili. Garantiamo l'utilizzo esclusivo di ricambi originali certificati, essenziali per ripristinare la silenziosità e l'efficienza energetica del tuo elettrodomestico. Offriamo un servizio rapido per ridurre al minimo il disagio di restare senza lavatrice, assicurando una riparazione duratura e coperta da garanzia."""
        },
        'Frigoriferi': {
            'short': "Intervento rapido su ricariche gas, termostati e sensori No-Frost.",
            'desc': """Un frigorifero che non raffredda adeguatamente o che genera ghiaccio in eccesso rappresenta un rischio per la conservazione dei tuoi alimenti. I nostri tecnici intervengono con urgenza su frigoriferi domestici e combinati, diagnosticando problemi legati alla perdita di gas refrigerante, guasti al compressore o malfunzionamenti del termostato.
Siamo specializzati nei moderni sistemi No-Frost, dove spesso i sensori di temperatura o le ventole di ricircolo possono bloccarsi. Una riparazione tempestiva è cruciale per evitare il deterioramento dei cibi e sprechi costosi. Utilizziamo strumentazione all'avanguardia per individuare micro-perdite nel circuito e sostituire le guarnizioni usurate che compromettono l'isolamento termico. Affidati alla nostra esperienza per ripristinare la temperatura ideale e l'efficienza del tuo frigorifero in tempi rapidi."""
        },
        'Lavastoviglie': {
            'short': "Risoluzione ostruzioni, problemi pompa e perdite d'acqua con ricambi originali.",
            'desc': """La tua lavastoviglie non lava bene, lascia residui o perde acqua sul pavimento? Spesso questi problemi sono causati da ostruzioni nei bracci rotanti, filtri intasati o malfunzionamenti della pompa di scarico. Il nostro servizio di assistenza a Como si occupa di ripristinare le prestazioni ottimali del tuo elettrodomestico, intervenendo anche su guasti alla resistenza che impediscono all'acqua di scaldarsi.
Utilizziamo ricambi originali per sostituire pompe, elettrovalvole e guarnizioni danneggiate. Inoltre, offriamo consulenza sull'uso corretto di detergenti e decalcificanti professionali per prevenire l'accumulo di calcare, nemico numero uno delle lavastoviglie. Un intervento professionale non solo risolve il guasto immediato, ma prolunga la vita utile dell'apparecchio, garantendo stoviglie brillanti e igienizzate ad ogni ciclo."""
        },
        'Asciugatrici': {
            'short': "Manutenzione condotti, sostituzione cinghie e prevenzione surriscaldamento.",
            'desc': """L'asciugatrice è indispensabile, specialmente nei mesi invernali. Se noti che i panni restano umidi, i tempi di asciugatura si allungano o l'apparecchio si surriscalda, potrebbe esserci un problema nei sensori di umidità o nel sistema di ventilazione. I nostri tecnici sono qualificati per intervenire su asciugatrici a condensazione e a pompa di calore.
Effettuiamo una pulizia approfondita dei condotti della condensa e dei filtri, spesso causa di blocchi e rischi di surriscaldamento. Sostituiamo cinghie spezzate, tendicinghia rumorosi e schede di controllo difettose. La manutenzione corretta è vitale non solo per l'efficienza energetica, ma anche per la sicurezza domestica. Ripristiniamo il funzionamento perfetto della tua asciugatrice con ricambi garantiti, assicurandoti bucato morbido e asciutto in tempi brevi."""
        }
    }

    print("Inizio aggiornamento servizi...")
    
    for title, data in services_data.items():
        # Try to find exactly or with contains (case insensitive)
        service = Service.objects.filter(title__icontains=title).first()
        if service:
            print(f"Aggiornamento servizio: {service.title}")
            service.description = data['desc']
            service.short_description = data['short']
            service.save()
        else:
            print(f"ATTENZIONE: Servizio non trovato per '{title}'. Creazione in corso...")
            # Optional: Create if not exists, but usually we prefer to update existing
            Service.objects.create(
                title=title,
                slug=title.lower(),
                description=data['desc'],
                short_description=data['short'],
                image='services/placeholder.jpg' # Placeholder
            )

    print("Aggiornamento completato!")

if __name__ == '__main__':
    update_services()
