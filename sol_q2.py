'''
Author: Artur Assis Alves
Date: 08/03/2023
Title: Is Fib
'''

'''
2) Dado a sequencia de Fibonacci, onde se inicia por 0 e 1 e o proximo valor sempre sera a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um numero, ele calcule a sequencia de Fibonacci e retorne uma mensagem avisando se o numero informado pertence ou nao a sequencia.

IMPORTANTE:
Esse numero pode ser informado atraves de qualquer entrada de sua preferwncia ou pode ser previamente definido no codigo;
'''


def _is_fib(num:int)->bool:
    #Check type:
    if not isinstance(num, int):
        raise TypeError("the input must be an int")
    an0, an1 = 0, 1
    an2 = 1
    #Trivial cases:
    if num < 0: return False
    if num in {an0, an1}: return True

    while num > an2:
        #Update an2:
        an0 = an1
        an1 = an2
        an2 = an0 + an1

    if num == an2: return True
    return False


def is_fib(num):
    if _is_fib(num): print(f"The number {num} is a Fibonacci number.")
    else: print(f"The number {num} is not a Fibonacci number.")


###############################################################################
#                                  TEST CASE                                  #
###############################################################################
import unittest
'''
Function name: _is_fib (_IF)
ID: _IF 
'''
class Test_IF(unittest.TestCase):
    '''
    Test cases:
    _IF000 - Test the function _IF with some edge cases inputs.

    _IF001 - Test the function _IF with some edge cases inputs.

    _IF002 - Test the function _IF with some general cases of each different class
           of equivalence.

    '''
    def test__IF000(self):
        with self.assertRaises(TypeError):
            _is_fib('a')
        with self.assertRaises(TypeError):
            _is_fib(None)

    def test__IF001(self):
        self.assertTrue(_is_fib(0))
        self.assertTrue(_is_fib(1))
        self.assertTrue(_is_fib(2))
        self.assertTrue(_is_fib(3))
        
        self.assertFalse(_is_fib(-1))
        self.assertFalse(_is_fib(4))
        self.assertFalse(_is_fib(6))

    def test__IF002(self):
        self.assertTrue(_is_fib(21))
        self.assertTrue(_is_fib(34))

        self.assertFalse(_is_fib(-1000))
        self.assertFalse(_is_fib(35))



if __name__=='__main__':
    unittest.main(argv=[''], verbosity=3,exit=False)
    print("\n\nResults:")
    is_fib(0)
    is_fib(1)
    is_fib(2)
    is_fib(3)
        
    is_fib(-1)
    is_fib(4)
    is_fib(6)
    is_fib(21)
    is_fib(34)

    is_fib(-1000)
    is_fib(35)
