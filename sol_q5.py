'''
Author: Artur Assis Alves
Date: 08/03/2023
Title: reverse string
'''

'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada atraves de qualquer entrada de sua preferencia ou pode ser previamente definida no codigo;
b) Evite usar funcoes prontas, como, por exemplo, reverse;
'''


def reverse_str(strn:str)->str:
    #Check type:
    if not isinstance(strn, str):
        raise TypeError("the input must be an str")


    str_builder = [] 
    strn_len = len(strn)
    for i in range(strn_len):
        str_builder.append(strn[strn_len - 1 - i])
    return ''.join(str_builder)





###############################################################################
#                                  TEST CASE                                  #
###############################################################################
import unittest
'''
Function name: reverse_str (RS)
ID: RS 
'''
class TestRS(unittest.TestCase):
    '''
    Test cases:
    RS000 - Test the function RS with some edge cases inputs.

    RS001 - Test the function RS with some edge cases inputs.

    RS002 - Test the function RS with some general cases of each different class
           of equivalence.

    '''
    def test_RS000(self):
        with self.assertRaises(TypeError):
            reverse_str(123)
        with self.assertRaises(TypeError):
            reverse_str(None)

    def test_RS001(self):
        self.assertEqual(reverse_str(''), '')
        self.assertEqual(reverse_str('a'), 'a')
        self.assertEqual(reverse_str('aa'), 'aa')
        self.assertEqual(reverse_str('ab'), 'ba')
        self.assertEqual(reverse_str('abc'), 'cba')

    def test_RS002(self):
        self.assertEqual(reverse_str('banana'), 'ananab')
        self.assertEqual(reverse_str('arara'), 'arara')
        self.assertEqual(reverse_str('abbfnd'), 'dnfbba')



if __name__=='__main__':
    unittest.main(argv=[''], verbosity=3,exit=False)
    print("\n\nResults:")
    s = 'a'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = 'aa'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = ''
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = 'abc'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = 'banana'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = 'abcdef'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
    s = 'arara'
    print(f"The string '{s}' reversed is '{reverse_str(s)}'")
