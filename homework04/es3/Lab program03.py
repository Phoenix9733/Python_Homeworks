'''
Un documento HTML puo' essere rappresentato sotto forma di albero, come visto a lezione, che si chiama DOM (Document Object Model).

Un qualsiasi nodo di questo albero puo' essere individuato sulla base delle proprie caratteristiche:
    - tag                       un tag del tipo indicato
    - .classe                   una delle parole presenti nel valore dell'attributo "class"
    - #id                       il valore dell'attributo "id"
    - @[attributo="valore"]     valore di un attributo generico
ed in base alla sua relazione con i tag che lo contengono:
    - avo discendente           il tag 'avo' contiene un tag 'discendente' a qualsiasi profondita'
    - padre > figlio            il tag 'padre' contiene il tag 'figlio' nel livello immediatamente sotto

Un selettore CSS e' una successione di selettori di tag separati da spazio che serve ad individuare uno o piu' nodi all'interno del DOM.
Esempio:
    div .class1 > #main_window
        seleziona un qualsiasi tag che ha                                       id="main_window"
        e' il figlio di un tag che ha                                            class="... class1 ..."
        e si trova all'interno (a qualsiasi livello di distanza) di un tag      div
Esempio2:
    p  table > tr > td > a
	seleziona un link (<a ...> </a>)
	figlio di una casella (<td> ... </td>)
	figlia di una riga (<tr> ... </tr>)
	figlia di una tabella (<table> ... </table>)
	contenuta a qualsiasi livello in un paragrafo (<p> .... </p>)

NOTA: questa definizione del CSS e' una versione ridottissima che non segue lo standard completo. 
In particolare, non e' possibile usare piu' relazioni '>' consecutive o costruire selettori alternativi (in OR) e selettori in AND.

Le modifiche da attuare su un DOM possono essere di 3 tipi:
    - conteggio dei nodi che soddisfano il selettore CSS
    - eliminazione di tutti i tag individuati da un selettore CSS
    - modifica degli attributi di tutti i tag individuati da un selettore CSS

Realizzate le funzioni che esplorano e modificano l'albero:
    conta_nodi(       fileIn, selettore)				
    elimina_nodi(       fileIn, selettore, fileOut)				
    cambia_attributo(	fileIn, selettore, chiave, valore, fileOut)

ATTENZIONE: nei test verra' utilizzato un timout globale di 1*N secondi (se il grader fa N test)
'''

from  my_html import HTMLNode, fparse


"""albero=fparse("page1-3.html")
def contatag(dom, tag):
    if dom.tag == '_text_':
        return 0
    res =0
    if dom.tag == tag:
        res+=1
    for figlio in dom.content:
        res+=contatag(figlio, tag)
    print(res)
    return res
def contattr (dom, attr):
    if dom.istext():
        return 0
    res=0
    if attr in dom.attr:
        res+=1
    for figlio in dom.content:
        res+=contattr(figlio, attr)
    print(res)
    return res"""
        
def trovaCSS (dom, selettore):
    primo = selettore[0]
    valore = selettore [1:]
    if dom.istext(): return False
    elif primo == '#':
        if 'id' in dom.attr and dom.attr['id']==valore:
            return True
    elif primo == '.':
        if 'class' in dom.attr and valore in dom.attr['class']:
            return True
    elif primo == '@':
        valore=valore.strip()
        a, v=valore.strip('[]')
        v=v.strip('"\'')
        if a in dom.attr and dom.attr[a]==v:
            return True
    else:
        return dom.tag == selettore 
    
    
    
def contaCSS (dom , selettore, ricorsione=True):
    sequenza = selettore.split()
    if dom.istext(): return 0
    if sequenza[0]=='>':
        contaCSS(dom, sequenza[1], ricorsione=False)
    if trovaCSS(dom, sequenza[0]):
        if not sequenza[1:]:
            return 1
        ret = 0 
        for figlio in dom.content:
            ret+=contaCSS(dom, sequenza[1:])
        return ret 
    ret=0
    if ricorsione:
        for figlio in dom.content:
            ret+=contaCSS(figlio, sequenza)
    return ret
        
        
    
    
def conta_nodi(fileIn, sequenza):
    radice = fparse(fileIn)
    sequenza = selettore.split()
    return contaCSS(radice, selettore)
    

def elimina_nodi(fileIn, selettore, fileOut):
    '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    '''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    #Inserite qui il vostro codice

