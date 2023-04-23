import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

DEBUG=True
DEBUG=False

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm,k, expected):
        '''Implementazione del test
            - fimm: il file in cui reperire l'immagine con la griglia
            - k: il lato del quadrati da contare
            - expected: la risposta attesa
        '''
        if DEBUG:
            result = program.es1(fimm, k)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.timeout(1), \
                    self.timer(1):
                result   = program.es1(fimm,k)
        self.assertEqual(type(result),  int,     "il risultato prodotto non e' un intero")
        self.assertEqual(result,        expected, "l'intero restituito non e' corretto")

    @data( ('1',       2,    2),  #  150 x  150 
           ('1',      20,    0),
           ('mini',    2,    2),  #  7x7
           ('2',       4,   10),  # 190 x 190
           ('3',       5,   54),  # 1040 x 540
           ('4',       7,  948),  # 2040 x 1040
           ('4_rimp',  7,  258),  # 2040 x 1040
           ('5',       1,    1),  # 1000 x 1000
           ('5',       2,    0),
           ('6',      22, 2291),  # 1000 x 1000
           #('6_bis',  40, 7475),  # 1000 x 1000
           ('6_ter',  40, 17871),  # 1000 x 1000
           ('raref',   1,    0), # 1000 x 500 
           ('raref',   2,    0),
           ('spars',   1,    1), # 1000 x 500 
           ('spars',   2,    0),
           ('spars', 200,    0),
           )
    @unpack
    def test_foto(self, ID, k, expected):
        filename = f'foto_{ID}.png'
        return self.do_test(filename,k,expected)

    
if __name__ == '__main__':
    Test.main()

