
# superdareof2020
Ottieni le rispose corrette da https://friend2020.com/it e diventa il miglior amico dell'anno con Python!

  **Prequisiti:**
    - python 2.7  (installalo da qui -> [Windows x86-64 MSI installer](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi) 
    - scapy library (dopo aver installato Python esegui questo comando dal Prompt dei comandi (CMD) -> `pip install scrapy`)

ora puoi avviare best_friend.py con il comando da CMD -> `scrapy runspider best_friend.py -s LOG_ENABLED=False` 

 Ricorda che con il CMD devi essere nella stessa directory in cui hai salvato il file, altrimenti usa il comando:
 `scrapy runspider [PERCORSO]\best_friend.py -s LOG_ENABLED=False` 
 dove sostituirai [PERCORSO] con il percorso assoluto per arrivare alla cartella in cui hai salvato best_friend.py (esempio C:\Users\TuoNome\Documents\).

## Piccola spiegazione
E' stato implementato, in una maniera estremamente semplice, un [web scraper](https://it.wikipedia.org/wiki/Web_scraping) che analizza il codice della pagina web di uno dei tanti [quiz dell'amicizia 2020](https://friend2020.com/it) e da essa ne ricava tutte le risposte corrette.

## **"COSA? Non ho capito."**

Ogni pagina web che visiti ti appare come una serie di immagini e parole scritte con cui molto spesso puoi interagire, giusto?
Affinché il tuo **browser** (Google Chrome, Mozilla Firefox, Internet Explorer, etc.) - **che è in realtà un'app/un programma** - possa capire **come** disporre i contenuti, **le pagine sono scritte in codice**, quindi in un particolare linguaggio di programmazione. Tu non te ne accorgi perchè ciò che vedi è il "risultato finale". Questo codice cioè viene *interpretato* dal browser, viene *eseguito*, e ciò che vedi è il *risultato* di tale operazione.
Per definire la **STRUTTURA**, quindi 'come devono essere disposti i contenuti in una pagina' si usa il linguaggio [**HTML**](https://it.wikipedia.org/wiki/HTML);
per definire l'**ESTETICA**, quindi i colori, tipografia, animazioni, etc. si utilizza il linguaggio [**CSS**](https://it.wikipedia.org/wiki/CSS).
Come è facilmente intuibile, **HTML e CSS** sono collegati tra loro, ***cooperano per insegnare al browser come mostrare i contenuti di una pagina web***.
il *web scraper* è **un programma che estrae specifiche informazioni da una di queste pagine web**, nel nostro caso quella che contiene le domande a cui dovremmo rispondere,  e da essa estrae tutte le risposte corrette, proprio perchè in alcuni casi come questo, **l'informazione è contenuta proprio nel codice HTML**.
Per programmarlo abbiamo usato il framework [Scrapy](https://scrapy.org/) che offre una serie di funzioni adeguate a raggiungere il nostro scopo.
