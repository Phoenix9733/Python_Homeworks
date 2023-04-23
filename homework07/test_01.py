import copy
import unittest
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm, expected):
        '''Implementazione del test
            - fimm: il file in cui reperire le stringhe
            - expected: la risposta attesa
            TIMEOUT: 1 secondo per ciascun test
        '''
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.forbidden_function('builtins.input'), \
                self.timeout(1), \
                self.timer(1):
            result   = program.es1(fimm,)
        self.assertEqual(type(result),  list,     "il risultato prodotto deve essere una lista")
        self.assertEqual(result,        expected, "la lista restituita non e' corretta")
        return 1

    @file_data("test_01.json")
    def test_json(self, filename, expected):
        return self.do_test(filename, expected)

    @file_data("test_random.json")
    def test_random(self, filename, lunghezza, expected):
        return self.do_test(filename, expected)

    @file_data("test_random_molte.json")
    def test_random2(self, filename, lunghezza, expected):
        return self.do_test(filename, expected)

    def test_4_ft5(self):
        '''terzo  test con ft5.txt '''
        lista4=[500]*2500
        return self.do_test('ft5.txt',lista4)

       
if __name__ == '__main__':
    Test.main()

