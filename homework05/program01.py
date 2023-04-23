'''
Si e' appena svolta una gara automobilistica con n piloti aventi per identificativi 
gli interi 1,2...n.
Nel corso della gara assistiamo a due tipi di eventi:
- il pilota i viene superato dal suo immediato inseguitore 
  (questo evento e' segnalato tramite una stringa 's'+str(i))
- il pilota i abbandona la gara 
  (questo evento e' segnalato dalla stringa 'e'+str(i))
Disponiamo di una  lista lista1 in cui sono raccolti sotto forma di stringhe e in ordine
temporale di occorrenza i due tipi di eventi:
-una stringa 's'+str(i) indica che il pilota i e' stato superato del suo immediato inseguitore.
-una stringa 'e'+str(i) indica che il pilota i abbandona la gara.
Disponiamo anche di una lista lista2 che riporta gli identificativi dei piloti nell'ordine 
in cui appaiono alla griglia di partenza ( in   lista2[i], 0<=i<n, troviamo 
l'identificativo del pilota che occupa l'i-ma posizione nella griglia di partenza).
Quindi il primo è in posizione 0.
Vogliamo ottenere una lista lista3 che riporti l'ordine d'arrivo  dei  piloti che portano a termine la gara
(se m piloti portano a termine la gara la lista lista3 avra' lunghezza m ed  
 lista3[i] sara' l'identificativo del pilota che nella gara arriva in posizione i-1).

Progettare una funzione es(lista1,lista2) che date
-lista 1: la lista dei due tipi di  eventi che si sono verificati nel corso della gara
-lista 2: la lista con le posizioni di partenza dei piloti
restituisce la lista contenente  gli identificativi dei  piloti che portano a termine la gara
in ordine di arrivo crescente. 
Attenzione, al termine dell'esecuzione della funzione le  liste lista1 e lista2 non  devono 
risultare modificate.
  
Ad esempio nel caso di:
lista1=['e2','s4','s3','s3','e1','s5'] e lista2=[5,3,2,4,1] i 6 eventi determinano i 
seguenti 6 cambiamenti nell'ordine di graduatoria:

5 ->e2-> 5 ->s4-> 5 ->s3-> 5 ->s3-> 5 ->e1-> 5->s5->4 
3        3        3        1        1        4      5
2        4        1        3        4        3      3
4        1        4        4        3
1                 

la funzione deve dunque restituire la lista [4,5,3]

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1.5 secondi per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)

'''
def es(lista1, lista2):
    dic=dictionary(lista2)
    lista3=[]
    for j in lista1:
        if j[0] == 'e':
            elemento_ricercato=dic.get(int(j[1:]))
            elemento_successivo=dic.get(elemento_ricercato[1])
            elemento_precedente=dic.get(elemento_ricercato[0])
            if elemento_successivo: elemento_successivo[0]=elemento_ricercato[0]
            if elemento_precedente: elemento_precedente[1]=elemento_ricercato[1]
            elemento_ricercato[0]=-1
            #print(dic)
        else:
            elemento_ricercato=dic.get(int(j[1:]))
            copia=elemento_ricercato[0]
            elemento_successivo=dic.get(elemento_ricercato[1])
            elemento_precedente=dic.get(elemento_ricercato[0])
            elemento_successivo1=dic.get(elemento_successivo[1])
            if elemento_successivo:
                elemento_ricercato[0]=elemento_ricercato[1]
                elemento_ricercato[1]=elemento_successivo[1]
                elemento_successivo[1]=elemento_successivo[0]
                elemento_successivo[0]=copia
            if elemento_precedente:
                elemento_precedente[1]=elemento_ricercato[0]
            if elemento_successivo1:
                elemento_successivo1[0]=elemento_successivo[1]  
    
    for key in dic.keys():
        if dic[key][0] == 0:
            lista3.append(key)
            break

    i=0 
    elemento=dic.get(lista3[0])
    
    
    while elemento[1]!=0:
        elemento=dic.get(lista3[i])
        if elemento[1]!=0:
            lista3.append(elemento[1])
        i+=1
    return lista3


def dictionary(lista2): 
    dic=dict()
    for i in range (0, len(lista2)): 
        if i == 0:
            dic.update({lista2[i]:[0,lista2[i+1]]})
        elif i==len(lista2)-1:
            dic.update({lista2[i]:[lista2[i-1], 0]})
        else:
            dic.update({lista2[i]:[lista2[i-1], lista2[i+1]]})
    return dic
    

print(es(['e2','s4','s3','s3','e1','s5'], [5,3,2,4,1]))
