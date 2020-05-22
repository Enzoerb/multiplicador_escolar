import unittest
import mult_escola_enzo
from random import randint


class TestMultEscola(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testes = [mult_escola_enzo.SchoolMult('0', '0'),
                      mult_escola_enzo.SchoolMult('4', '4'),
                      mult_escola_enzo.SchoolMult('10', '10'),
                      mult_escola_enzo.SchoolMult('111', '111'),
                      mult_escola_enzo.SchoolMult('1'*9, '1'*9),
                      mult_escola_enzo.SchoolMult('-'+'1'*9, '1'*9),
                      mult_escola_enzo.SchoolMult('1'*3+'.'+'1'*6, '1'*9),
                      mult_escola_enzo.SchoolMult('12345', '98765'),
                      mult_escola_enzo.SchoolMult('-12345', '98765'),
                      mult_escola_enzo.SchoolMult('-12345', '-98765'),
                      mult_escola_enzo.SchoolMult('12.345', '98765'),
                      mult_escola_enzo.SchoolMult('-12345', '98.765'),
                      mult_escola_enzo.SchoolMult('123.45', '9876.5'),
                      mult_escola_enzo.SchoolMult('-1.2345', '98.765')]
        for teste in cls.testes:
            teste.signal()
            teste.ten_potence()
            teste.mid_operation()
            teste.final_sum()

    def test_signal(self):
        self.assertEqual(self.testes[0].result_signal, 1)
        self.assertEqual(self.testes[1].result_signal, 1)
        self.assertEqual(self.testes[2].result_signal, 1)
        self.assertEqual(self.testes[3].result_signal, 1)
        self.assertEqual(self.testes[4].result_signal, 1)
        self.assertEqual(self.testes[5].result_signal, -1)
        self.assertEqual(self.testes[6].result_signal, 1)
        self.assertEqual(self.testes[7].result_signal, 1)
        self.assertEqual(self.testes[8].result_signal, -1)
        self.assertEqual(self.testes[9].result_signal, 1)
        self.assertEqual(self.testes[10].result_signal, 1)
        self.assertEqual(self.testes[11].result_signal, -1)
        self.assertEqual(self.testes[12].result_signal, 1)
        self.assertEqual(self.testes[13].result_signal, -1)

    def test_ten_potence(self):
        self.assertEqual(self.testes[0].potence, 0)
        self.assertEqual(self.testes[1].potence, 0)
        self.assertEqual(self.testes[2].potence, 0)
        self.assertEqual(self.testes[3].potence, 0)
        self.assertEqual(self.testes[4].potence, 0)
        self.assertEqual(self.testes[5].potence, 0)
        self.assertEqual(self.testes[6].potence, 6)
        self.assertEqual(self.testes[7].potence, 0)
        self.assertEqual(self.testes[8].potence, 0)
        self.assertEqual(self.testes[9].potence, 0)
        self.assertEqual(self.testes[10].potence, 3)
        self.assertEqual(self.testes[11].potence, 3)
        self.assertEqual(self.testes[12].potence, 3)
        self.assertEqual(self.testes[13].potence, 7)

    def test_potence_format(self):
        self.assertEqual(self.testes[0].potence_format('12345'), ('12345', 0))
        self.assertEqual(self.testes[0].potence_format('-12345'), ('12345', 0))
        self.assertEqual(self.testes[0].potence_format('+12345'), ('12345', 0))
        self.assertEqual(self.testes[0].potence_format('1234.5'), ('12345', 1))
        self.assertEqual(self.testes[0].potence_format('1.2345'), ('12345', 4))

    def test_mid_operation(self):
        self.assertEqual(self.testes[0].mid_numbers, ['0'])
        self.assertEqual(self.testes[1].mid_numbers, ['16'])
        self.assertEqual(self.testes[2].mid_numbers, ['0', '10'])
        self.assertEqual(self.testes[3].mid_numbers, ['1'*3]*3)
        result_4_till_6 = ['1'*9]*9
        self.assertEqual(self.testes[4].mid_numbers, result_4_till_6)
        self.assertEqual(self.testes[5].mid_numbers, result_4_till_6)
        self.assertEqual(self.testes[6].mid_numbers, result_4_till_6)
        result_7_till_13 = ['493825', '395060', '296295', '197530', '98765']
        self.assertEqual(self.testes[7].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[8].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[9].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[10].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[11].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[12].mid_numbers, result_7_till_13)
        self.assertEqual(self.testes[13].mid_numbers, result_7_till_13)

    def test_final_sum(self):
        self.assertEqual(self.testes[0].mid_sum, '0')
        self.assertEqual(self.testes[1].mid_sum, '16')
        self.assertEqual(self.testes[2].mid_sum, '100')
        self.assertEqual(self.testes[3].mid_sum, '12321')
        self.assertEqual(self.testes[4].mid_sum, '12345678987654321')
        self.assertEqual(self.testes[5].mid_sum, '12345678987654321')
        self.assertEqual(self.testes[6].mid_sum, '12345678987654321')
        self.assertEqual(self.testes[7].mid_sum, '1219253925')
        self.assertEqual(self.testes[8].mid_sum, '1219253925')
        self.assertEqual(self.testes[9].mid_sum, '1219253925')
        self.assertEqual(self.testes[10].mid_sum, '1219253925')
        self.assertEqual(self.testes[11].mid_sum, '1219253925')
        self.assertEqual(self.testes[12].mid_sum, '1219253925')
        self.assertEqual(self.testes[13].mid_sum, '1219253925')

        self.assertEqual(self.testes[0].result, '+0')
        self.assertEqual(self.testes[1].result, '+16')
        self.assertEqual(self.testes[2].result, '+100')
        self.assertEqual(self.testes[3].result, '+12321')
        self.assertEqual(self.testes[4].result, '+12345678987654321')
        self.assertEqual(self.testes[5].result, '-12345678987654321')
        self.assertEqual(self.testes[6].result, '+12345678987.654321')
        self.assertEqual(self.testes[7].result, '+1219253925')
        self.assertEqual(self.testes[8].result, '-1219253925')
        self.assertEqual(self.testes[9].result, '+1219253925')
        self.assertEqual(self.testes[10].result, '+1219253.925')
        self.assertEqual(self.testes[11].result, '-1219253.925')
        self.assertEqual(self.testes[12].result, '+1219253.925')
        self.assertEqual(self.testes[13].result, '-121.9253925')

    def test_len(self):
        self.assertEqual(len(self.testes[0]), 2)
        self.assertEqual(len(self.testes[1]), 3)
        self.assertEqual(len(self.testes[2]), 4)
        self.assertEqual(len(self.testes[3]), 6)
        self.assertEqual(len(self.testes[4]), 18)
        self.assertEqual(len(self.testes[5]), 18)
        self.assertEqual(len(self.testes[6]), 19)
        self.assertEqual(len(self.testes[7]), 11)
        self.assertEqual(len(self.testes[8]), 11)
        self.assertEqual(len(self.testes[9]), 11)
        self.assertEqual(len(self.testes[10]), 12)
        self.assertEqual(len(self.testes[11]), 12)
        self.assertEqual(len(self.testes[12]), 12)
        self.assertEqual(len(self.testes[13]), 12)

    def test_include_decimal(self):
        check_list = [self.testes[6].include_decimal(number, spaces)
                      for spaces, number in enumerate(self.testes[6].mid_numbers)]

        result = ['1'*9]*3
        result = [number + ' ' for number in result]
        result = ['1'*(9-number)+'.'+'1'*(decimal-3)
                  for number, decimal in zip(range(6, 0, -1), range(9, 3, -1))] + result
        result = [number + ' '*spaces for spaces, number in enumerate(result)]

        self.assertEqual(check_list, result)

    def test_str(self):
        result_0 = '\n'.join(['   0',
                              'x  0',
                              '-----',
                              '  +0',
                              '-----',
                              '  +0'])

        result_1 = '\n'.join(['    4',
                              'x   4',
                              '------',
                              '  +16',
                              '------',
                              '  +16'])

        result_2 = '\n'.join(['    10',
                              'x   10',
                              '-------',
                              '    +0',
                              '  +10 ',
                              '-------',
                              '  +100'])

        result_3 = '\n'.join(['     111',
                              'x    111',
                              '---------',
                              '    +111',
                              '   +111 ',
                              '  +111  ',
                              '---------',
                              '  +12321'])

        result_7 = '\n'.join(['        98765',
                              'x       12345',
                              '--------------',
                              '      +493825',
                              '     +395060 ',
                              '    +296295  ',
                              '   +197530   ',
                              '   +98765    ',
                              '--------------',
                              '  +1219253925'])

        result_8 = '\n'.join(['        98765',
                              'x      -12345',
                              '--------------',
                              '      -493825',
                              '     -395060 ',
                              '    -296295  ',
                              '   -197530   ',
                              '   -98765    ',
                              '--------------',
                              '  -1219253925'])

        result_13 = '\n'.join(['        98.765',
                               'x      -1.2345',
                               '---------------',
                               '    -0.0493825',
                               '    -0.395060 ',
                               '    -2.96295  ',
                               '   -19.7530   ',
                               '   -98.765    ',
                               '---------------',
                               '  -121.9253925'])

        self.assertEqual(str(self.testes[0]), result_0)
        self.assertEqual(str(self.testes[1]), result_1)
        self.assertEqual(str(self.testes[2]), result_2)
        self.assertEqual(str(self.testes[3]), result_3)
        self.assertEqual(str(self.testes[7]), result_7)
        self.assertEqual(str(self.testes[8]), result_8)
        self.assertEqual(str(self.testes[13]), result_13)


if __name__ == '__main__':
    unittest.main()
