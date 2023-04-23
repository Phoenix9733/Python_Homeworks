# -*- coding: utf-8 -*-
''' 
    In un immagine a sfondo nero  e' disegnata  una griglia  
    dove  alcuni segmenti che ne connettono i nodi in orizzontale 
    o in verticale sono stati cancellati (i nodi della griglia sono in 
    verde mentre i segmenti sono in rosso).
    La dimensione del lato dei quadrati della griglia non è data.

    Si veda ad esempio la figura foto_1.png.
    Progettare la funzione es1(fimm, k) che prende in input l'indirizzo 
    dell'immagine contenente la griglia ed un intero k e restituisce un intero. 
    L'intero restituito e' il numero di 
    quadrati rossi (con pixel verdi) di lato k (steps della griglia) che sono presenti nell'immagine.
    Ad esempio  es1(foto_1.png,2) deve restituire 2 (i due quadrati rossi presenti nella 
    sottogriglia hanno il vertice in alto a sinistra con coordinate (3,0) e 
    (4,2) nelle coordinate della griglia, rispettivamente)

    Per caricare e salvare  file PNG si possono usare load e save della libreria immagini allegata.

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)

'''
from immagini import*
verde = (  0, 255,   0)
rosso = (255,   0,   0)
nero  = (  0,   0,   0)

def dentro(img, x, y):
    return 0<=x<len(img[0]) and 0<=y<len(img)

def lat(img, x, y):
    lato=0
    while dentro(img, x, y)==True and (img[x][y]==rosso or img[x][y]==nero):
        lato=lato+1
        y=y+1
        print 
    return lato

def conta_rossi(img):
    conta_rosso=0
    for j in range(len(img)):
        for d in range(len(img[0])):
            if img[j][d]==verde:
                n, o = j, d
            if img[j][d]==rosso:
                conta_rosso+=1
    return conta_rosso, n, o

def es1(fimm,k):
    img=load(fimm)
    lato=0
    conta_validi=0
    for j in range(len(img)):
        for d in range(len(img[0])):
            if img[j][d]==verde:
                x, y = j, d
                lato=lat(img, j, d+1)+1
                break
        if img[j][d]==verde:
            break
    conta_rosso, ultima_x, ultima_y = conta_rossi(img)
    prima_y=y
    if conta_rosso>=k*4:
        while x<ultima_x or y<ultima_y: 
                if quadrato_valido(img, lato, x, y, k):
                    conta_validi+=1
                y+=lato
                if y>ultima_y:
                    x+=lato
                    y=prima_y
                if x>ultima_x:
                    break
    return conta_validi   
        
            



def quadrato_valido(img,lato, x, y, k):
    mass_x=len(img)
    mass_y=len(img[0])
    riga=0
    colonna=0
    p1=True
    p2=True
    last_x=x+(lato*k)
    last_y=y+(lato*k)
    if x>mass_x-(k*lato) or y>mass_y-(k*lato):
        return False
    
    if lato>1:
        for riga in range(x, last_x, k):
            for colonna in range(y+1,len(img[0]), k):
                   p2=img[riga][colonna]!=nero and p2
                   if p2==False:
                       break
            if p2==False:
                break
        if p2==True:
            return p2
        
    
    if k==1 and lato==1 and x+2 < mass_x and y+2< mass_y:
        p1=img[x][y+1]==rosso
        p2=img[x+1][y+2]==rosso
        p3=img[x+1][y]==rosso
        p4=img[x+2][y+1]==rosso
        return p1 and p2 and p3 and p4
    
    else:
        for riga in range(x, last_x+1, lato):
            for colonna in range(y, last_y+1 , lato):
            
                    if riga==x and colonna < last_y :
                        p1= p1 and img[riga][colonna+1]==rosso
                        
                    elif (riga !=x and (colonna == last_y or colonna==y)):
                        p1= p1 and img[riga-1][colonna]==rosso
                        
                    elif (colonna==last_y and riga!=x):
                        p1= p1 and img[riga-1][colonna]==rosso
                        
                    if (riga==last_x and colonna!=last_y):    
                        p1= p1 and img[riga][colonna+1]==rosso
        
        return p1