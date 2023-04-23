import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm,a,b,n, expected):
        '''Implementazione del test
            - fimm: il file in cui reperire la sequenza
            - a,b: gli estremi dell'intervallo delle lunghezze delle sottosequenze
            - n: il numero massimo di frequenze
            - expected: la risposta attesa
            TIMEOUT: 1 secondo per ciascun test
        '''
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.forbidden_function('builtins.input'), \
                self.timeout(1), \
                self.timer(1):
            result   = program.es1(fimm,a,b,n)
        self.assertEqual(type(result),  list,     "il risultato prodotto deve essere una lista")
        self.assertEqual(type(result[0]),  tuple,     "la lista restituita deve contenere tuple")
        self.assertEqual(type(result[0][0]),  int,     "la prima coordinata delle tuple restituite deve essere un intero")
        self.assertEqual(type(result[0][1]),  list,     "la seconda  coordinata delle tuple restituite deve essere una lista")
        self.assertEqual(type(result[0][1][0]),  str,     "la seconda  coordinata delle tuple deve contenere una lista di stringhe")
        self.assertEqual(result,        expected, "la lista restituita non e' corretto")
        return 1

    @file_data("test_01.json")
    def test_json(self, filename, da, a, n, expected):
        expected = list(map(tuple,expected))
        return self.do_test(filename, da, a, n, expected)
   
    @file_data("test_random.json")
    def test_random(self, filename, da, a, n, expected):
        expected = list(map(tuple,expected))
        return self.do_test(filename, da, a, n, expected)

if __name__ == '__main__':
    Test.main()

