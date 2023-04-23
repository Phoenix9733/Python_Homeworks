
def es(lista1, lista2):
    lista3=lista2.copy()
    for j in lista1:
        indice=lista3.index(int(j[1:]))
        if j[0] == 'e':
            lista3.pop(indice)
        else:
            lista3[indice], lista3[indice+1] = lista3[indice+1], lista3[indice]
    return lista3


def es(lista1, lista2):
    dic=dictionary(lista2)
    lista3=[]
    #print(dic)
    for j in lista1:
        if j[0] == 'e':
            elemento_ricercato=dic.get(int(j[1:]))
            if elemento_ricercato[0]>-1 and elemento_ricercato[1]> -1:
                
                elemento_successivo=dic.get(elemento_ricercato[1])
                if elemento_successivo: elemento_successivo[0]=elemento_ricercato[0]
                elemento_precedente=dic.get(elemento_ricercato[0])
                if elemento_precedente: elemento_precedente[1]=elemento_ricercato[1]
            if elemento_ricercato:
                elemento_ricercato[0]=-1
                elemento_ricercato[1]=-1
    
                   
        '''else:
            elemento_ricercato=dic.get(int(j[1:]))
            
            copia=list(elemento_ricercato)
            if elemento_ricercato: 
                print(dic)
                elemento_successivo=dic.get(elemento_ricercato[1])
                if elemento_successivo:
                    elemento_ricercato=list(elemento_successivo)
                    elemento_successivo=list(copia)
                    #elemento_ricercato[1]=elemento_successivo[1]
                    #elemento_ricercato[0]=elemento_successivo[0]
                    #elemento_successivo[0]=copia[0]
                    #elemento_successivo[1]=copia[1]
                    print('==========================')
                    for key, value in dic.items():
                        print( '--->' + str(value[0]))
                        print(key)
                        print( '--->' + str(value[1]))
                        print('==========================')
                    
   #             dic.update({int(j[1:]), elemento_successivo[0], elemento_successivo[1]})
    #            dic.update({elemento_successivo[0], elemento_ricercato[0], elemento_ricercato[1]})
     #       print(dic)'''
    print(dic)
    lista5=[]
    for key, value in dic.items():
        if value[0]!=-1:
            lista5.append(key)
            
    lista3=lista5.copy()
    for j in lista1:
        if j[0] == 's':
            indice=lista3.index(int(j[1:]))
            #print(indice)
            #print(lista3)
            if indice < len(lista3)-1:
                lista3[indice], lista3[indice+1] = lista3[indice+1], lista3[indice]
    
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


print(es(['e2','s4', 's3', 's3', 'e1', 's5'], [5,3,2,4,1]))
