import unittest
import mult_escola_enzo
from random import randint, choice


class TestMultEscola(unittest.TestCase):

    def test_mid_operation(self):
        first_result = ['1', '493825', '395060'+(' '*1),
                        '296295'+(' '*2), '197530'+(' '*3), '98765'+(' '*4)]
        second_result = ['-1'] + first_result[1:]

        self.assertEqual(mult_escola_enzo.mid_operation(98765, 12345), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-98765, -12345), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-98765, 12345), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation(98765, -12345), second_result)

        self.assertEqual(mult_escola_enzo.mid_operation('98765', '12345'), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-98765', '-12345'), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-98765', '12345'), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation('98765', '-12345'), second_result)

        self.assertEqual(mult_escola_enzo.mid_operation(0, 0), ['1', '0'])

    def test_final_sum(self):
        first_input = ['1', '493825', '395060'+(' '*1),
                       '296295'+(' '*2), '197530'+(' '*3), '98765'+(' '*4)]
        second_input = ['-1'] + first_input[1:]
        self.assertEqual(mult_escola_enzo.final_sum(first_input), 1219253925)
        self.assertEqual(mult_escola_enzo.final_sum(second_input), -1219253925)
        self.assertEqual(mult_escola_enzo.final_sum(['1', '0']), 0)

    def test_school_multiplication(self):
        self.assertEqual(mult_escola_enzo.school_multiplication(98765, 12345), 1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(-98765, 12345), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(98765, -12345), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(-98765, -12345), 1219253925)

        self.assertEqual(mult_escola_enzo.school_multiplication('98765', '12345'), 1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('-98765', '12345'), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('98765', '-12345'), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('-98765', '-12345'), 1219253925)

        self.assertEqual(mult_escola_enzo.school_multiplication(0, 0), 0)

        for test in range(10):
            number_1 = 0
            number_2 = 0
            for size in range(randint(1, 10)):
                number_1 += randint(0, 9)*10**size
                signal = choice([1, -1])
                number_1 *= signal

            for size in range(randint(1, 10)):
                number_2 += randint(0, 9)*10**size
                signal = choice([1, -1])
                number_2 *= signal

            multiplication = number_1 * number_2
            self.assertEqual(mult_escola_enzo.school_multiplication(
                number_1, number_2), multiplication)
            self.assertEqual(mult_escola_enzo.school_multiplication(
                str(number_1), str(number_2)), multiplication)


if __name__ == '__main__':
    unittest.main()
