import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, lista1,lista2,expected):
        '''Implementazione del test
            - lista1 e lista2: le due liste di input 
            - expected: la lista attesa
            TIMEOUT: 1.5 secondi per ciascun test
        '''
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.forbidden_function('builtins.input'), \
                self.timer(1.5):
            l1=lista1.copy()
            l2=lista2.copy()
            result   = program.es(l1,l2)
        self.assertEqual(lista1,  l1,     "la lista di input lista1 non va modificata")
        self.assertEqual(lista2,  l2,     "la lista di input lista2 non va modificata")
        self.assertEqual(type(result),  list,     "il risultato prodotto non e' una lista")
        self.assertEqual(result,        expected, "la lista  restituita non e' corretta")

    @file_data("test_01.json")
    def test_json(self, azioni, concorrenti, expected):
        return self.do_test(azioni, concorrenti, expected)

    def test_1_esempio2(self):
        '''Istanza con 20 concorrenti.  
        Senza alcun sorpasso i piloti abbandonano uno dopo 
        l'altro a partire da quello in prima posizione  e resta l'ultimo.
        la funzione deve restituire la lista [20]
         '''
        n=20
        lista2=[x+1 for x in range(n)]
        lista1=['e'+str(i) for i in range(1,n)] 
        return self.do_test(lista1,lista2, [20])

    def test_1_esempio3(self):
        '''Istanza con 15 concorrenti.  
        La classifica iniziale di 15 auto viene 
        completamente ribaltata e poi abbandonano tutti tranne gli ultimi 10.
        La funzione deve restituire la lista [10,9, 8, 7, 6, 5, 4, 3, 2, 1]
         '''
        n=15
        lista2=[x+1 for x in range(n)]
        lista1=['s'+str(n-i) for j in range(1,n) for i in range(j,n)]
        for i in reversed(range(11,n+1)): lista1.append('e'+str(i))
        return self.do_test(lista1,lista2, [10,9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_1_esempio4(self):
        '''Istanza con 200000 concorrenti.  
        Senza alcun sorpasso i piloti abbandonano uno dopo 
        l'altro a partire da quello in prima posizione  e resta l'ultimo.
        la funzione deve restituire la lista [200000]
         '''
        n=200000
        lista2=[x+1 for x in range(n)]
        lista1=['e'+str(i) for i in range(1,n)] 
        return self.do_test(lista1,lista2, [200000])

    def test_1_esempio5(self):
        '''Istanza con 1500 concorrenti.  
        La classifica iniziale di 1500 auto viene 
        completamente ribaltata e poi abbandonano tutti tranne gli ultimi 10.
        La funzione deve restituire la lista [10,9, 8, 7, 6, 5, 4, 3, 2, 1]
         '''
        n=1500
        lista2=[x+1 for x in range(n)]
        lista1=['s'+str(n-i) for j in range(1,n) for i in range(j,n)]
        for i in reversed(range(11,n+1)): lista1.append('e'+str(i))
        return self.do_test(lista1,lista2, [10,9, 8, 7, 6, 5, 4, 3, 2, 1])

if __name__ == '__main__':
    Test.main()

