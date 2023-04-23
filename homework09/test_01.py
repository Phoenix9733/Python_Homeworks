import testlib
import isrecursive
from ddt import file_data, ddt, data, unpack


DEBUG = True
DEBUG = False

@ddt
class Test(testlib.TestCase):

    def do_test(self, filename, expected):
        '''Implementazione del test
            - ftesto: il file in cui reperire la matrice e la lista delle parole
            - expected: la lista attesa
        '''
        expected = [ x if x==-1 else tuple(x) for x in expected ]
        if DEBUG:
            import program01 as program
            result   = program.es1(filename)
        else:
            # prima controlliamo che l'implementazione sia ricorsiva
            try:
                import program01 as program
                isrecursive.decorate_module(program)
                program.es1(filename)
            except isrecursive.RecursionDetectedError:
                pass
            else:
                raise Exception("Recursion not present")
            finally:
                isrecursive.undecorate_module(program)
                del program

            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.check_open({filename : ['r']}), \
                    self.check_imports( allowed=['program01','encodings.utf_8','encodings.utf_8_sig']), \
                    self.timeout(1), \
                    self.timer(1):
                import program01 as program
                result   = program.es1(filename)
        self.assertIsInstance(result,   list,     "il risultato prodotto non e' una lista")
        self.assertEqual(result,        expected, "la lista  restituita non e' corretta")

    @file_data('test_01.json')
    def test_json(self, filename, expected):
        return self.do_test(filename,expected)

if __name__ == '__main__':
    Test.main()
