
'''
    Data una matrice di caratteri ed una parola, diciamo che la  parola e' presente
    nella matrice se e' possibile ottenerla collezionando i caratteri
    che si incontrano con una serie di spostamenti tra celle adiacenti.
    I soli spostamenti permessi sono:
    a) da una cella alla cella adiacente a destra (D)
    b) da una cella alla cella in basso (G)
    la parola, se presente nella matrice, e'  individuata dalle coordinate
    di riga e colonna della cella da cui si parte e dalla stringa di 'D' e 'G'
    che denota la sequenza di spostamenti da effettuare per collezionare i suoi caratteri.

    Si consideri ad esempio la matrice

      ANTANDBER
      LNOANRLNT
      EIOSGEARO
      SSUNALSIC
      AANDEOAAO

    in questa matrice:
    'ANGELO' e' presente ed e' individuata da (1,3) e 'DGDGG'
    'ANDREA' e' presente ed e' individuata da (0,3) e 'DDGGD'
    'ENRICO' e' presente ed e' individuata da (0,7) e 'GGGDG'
    'ALESSANDRO', 'ANTONIO' e 'ALBERTO' sono parole non presenti.

    Abbiamo una matrice ed una lista di parole e vogliamo sapere quali sono presenti
    nella matrice e quali no.

    Progettare una funzione es1(ftesto) che preso l'indirizzo di un file
    di testo in cui e' registrata la matrice e la lista di parole da ricercare e
    restituisce una lista.
    Nella lista restituita all'i-esimo posto troviamo:
    - -1 se la parola non e' presente nella matrice.
    - la posizione dell'i-esima parola della lista nella matrice
      (vale a dire la terna (riga,colonna,s) con (riga,colonna) coordinate iniziali
      della cella d'inizio degli spostamenti ed s stringa che denota gli spostamenti).
      Nel caso la parola sia presente piu' volte nella matrice deve essere restituita
      la posizione piu' in alto  a sinistra in cui compare e nel caso compaia
      piu' volte a partire dalla stessa casella delle diverse stringhe che
      la individuano va presa quella che precede le altre lessicograficamente.

    Ad esempio, Per la matrice vista  sopra e la lista
    ['ALBERTO','ALESSANDRO','ANDREA', 'ANGELO', 'ANTONIO', 'ENRICO']
    la funzione es1 restituira' la lista
    [-1,-1,(0,3, 'DDGGD'),(1,3, 'DGDGG'),-1,(0,7, 'GGGDG')]

    Il file ftesto  contiene  la matrice  e, di seguito  l'elenco delle parole.
    Una serie di 1 o piu'  linee vuote precede la reppresentazione della matrice,
    separa il diagramma dall'elenco delle parole e segue l'elenco delle parole.
    La matrice  e' registrata per righe (una riga per linea e in linee consecutive) gli
    elementi di ciascuna riga sono adiacenti a formare una stringa.
    La lista delle parole occupa  invece linee consecutive con  una o piu' parole o
    separate da spazi per ciascuna linea.
    Per un esempio si veda il file esempio_Disney.pdf

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    NOTA: almeno una delle funzioni realizzate DEVE essere ricorsiva, ad esempio
    potete scandire la matrice iterativamente e le lettere della parola cercata ricorsivamente.

    NON usate nessuna libreria.

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''

def matrix(f):
    matrice=[]
    parole=[]
    cont=0
    for k in f:
        if k=='\n':
            if len(matrice)>0:
                cont=1
        elif cont==0 :
            matrice+=k.split()
        else:
            parole+=k.split()
    return matrice, parole


def es1(ftesto):
    percorso=''
    indice_parola=0
    cont=0
    lista_finale=[]
    with open (ftesto) as f:
        f=f.readlines()
    matrice, parole=matrix(f)
    for parola in parole:
        lista_finale.append(-1)  
        for riga in range(0, len(matrice)):
            for colonna in range(0, len(matrice[0])):
                if parola[0]==matrice[riga][colonna]:
                    check=cerca_R_D(parola, riga, colonna, indice_parola, matrice, percorso, cont)
                    check2=cerca_D_R(parola, riga, colonna, indice_parola, matrice, percorso, cont)
                    if check:
                        lista_finale[len(lista_finale)-1]=(riga, colonna, check)
                        break
                    elif check2:
                        lista_finale[len(lista_finale)-1]=(riga, colonna, check2)
                        break
            if check or check2:
                check=False
                check2=False
                break
    return lista_finale
                 
        
def cerca_R_D (parola, riga, colonna, indice_parola, matrice, percorso, cont):
    lunghezza=len(parola)
    cont+=1
    if cont==lunghezza:
        return percorso
    else:
        #Verifico l'elemento a DX 
        if colonna+1<len(matrice[0]) and parola[indice_parola+1]==matrice[riga][colonna+1]:
            percorso+='D'
            return cerca_R_D (parola, riga, colonna+1, indice_parola+1, matrice, percorso, cont)
        else:
            #Verifico l'elemento a GIU 
            if riga+1<len(matrice) and parola[indice_parola+1]==matrice[riga+1][colonna]:
                percorso+='G'
                return cerca_R_D(parola, riga+1, colonna, indice_parola+1, matrice, percorso, cont)
            elif len(percorso)<len(parola)-2 and riga+1<len(matrice) and parola[indice_parola]==matrice[riga+1][colonna-1]:
                percorso=percorso[:-1]
                cont-=1
                percorso+='G'
                return cerca_R_D(parola, riga+1, colonna-1, indice_parola, matrice, percorso, cont)
            
def cerca_D_R (parola, riga, colonna, indice_parola, matrice, percorso, cont):
    lunghezza=len(parola)
    cont+=1
    if cont==lunghezza:
        return percorso
    
    else:
        #Verifico l'elemento a GIU 
        if riga+1<len(matrice) and parola[indice_parola+1]==matrice[riga+1][colonna]:
                percorso+='G'
                return cerca_D_R(parola, riga+1, colonna, indice_parola+1, matrice, percorso, cont)
        
        else:
            #Verifico l'elemento a GIU 
            if len(percorso)<len(parola)-2 and colonna+1<len(matrice[0]) and parola[indice_parola]==matrice[riga-1][colonna+1]:
                percorso=percorso[:-1]
                cont-=1
                percorso+='D'
                return cerca_D_R (parola, riga-1, colonna+1, indice_parola, matrice, percorso, cont)
            elif colonna+1<len(matrice[0]) and parola[indice_parola+1]==matrice[riga][colonna+1]:
                percorso+='D'
                return cerca_D_R (parola, riga, colonna+1, indice_parola+1, matrice, percorso, cont)

