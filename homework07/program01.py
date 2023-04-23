
''' 
    Abbiamo n stringhe di caratteri.  
    All'interno delle stringhe  e' nascosta una parola segreta come sottostringa di 
    caratteri consecutivi. 
    Sappiamo con certezza che la parola si ripete uguale esattamente una volta in ciascuna 
    stringa ma non sappiamo dove. 
    Della parola conosciamo la lunghezza M e sappiamo che non ci sono altre sottostringhe 
    di lunghezza M che si ripetono una sola volta in tutte le stringhe. 
    Vogliamo sapere per ogni stringa  la posizione dove compare il primo carattere 
    della parola nascosta.
    Ad esempio per le 6 stringhe con parola nascosta di lunghezza 3:
    
    moneta
    maratoneta
    pitone
    onesto
    storione
    sonetto
    
    la parola nascosta è 'one' e le posizioni sono nell'ordine: 1, 5, 3, 0, 5, 1
    

    
    Progettare una funzione es1(ftesto) che prende in input  un file contenente la lunghezza 
    della parola nascosta e le n stringhe di caratteri e restituisce una lista di n interi.
    L'intero in  posizione i della lista e' la posizione dove compare il primo carattere 
    della parola nascosta nella stringa i. 
    
    Le informazioni nel file ftesto sono organizzate nel seguente modo:
    - la prima riga contiene la lunghezza della parola nascosta (un intero).
    - seguono poi le stringhe di caratteri, ciascuna stringa occupa una o piu' 
    righe consecutive del file ed e' separata dalla stringa seguente da una linea vuota.
    Ogni riga del file termina con un' andata a capo.
    Vedi ad esempio il file ft1.txt che codifica l'istanza vista prima.
    
    es('ft1.txt') deve restituire la lista [1,5,3,0,5,1]    
   

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)
   
'''

def es1(ftesto):
    with open (ftesto) as f:
        f=f.readlines()
    lista_index=[]
    numero_seg=f[0]
    parole=ordinare_parole (f, numero_seg)
    parola_seg=parola_segreta (parole, numero_seg)
    for i in parole:
        index=i.find(parola_seg)
        lista_index.append(index)
    return lista_index
        


def seg(stem, res, parole, n):
    for k in range(1, n):
        if parole[0]!=parole[k]:
                    if stem not in parole[k]:
                        break
                    if parole[k].count(stem)>1:
                        break
                    if k + 1 == n:
                        res = stem
    return res


def parola_segreta(parole, numero_seg):
    n = len(parole)  
    s = parole[0] 
    l = len(s) 
    numero_seg=int(numero_seg)
    res =''
    for i in range(l) :
        stem = s[i:numero_seg] 
        seg1=seg(stem, res, parole, n)
        if seg1!='':
            break
        numero_seg+=1
    return seg1

def ordinare_parole (f, numero_seg):
    appoggio=''
    parole=[]
    f+='\n'
    f.remove(numero_seg)
    for k in f:
        if k != '\n':
            appoggio+=k
            appoggio="".join(line.strip() for line in appoggio)
        if k == '\n':
            parole.append(appoggio)
            appoggio=''
    return parole