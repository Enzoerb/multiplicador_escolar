import unittest
import mult_escola_enzo
from random import randint


class TestMultEscola(unittest.TestCase):

    def test_signal(self):
        self.assertEqual(mult_escola_enzo.signal(98765), 1)
        self.assertEqual(mult_escola_enzo.signal(-98765), -1)
        self.assertEqual(mult_escola_enzo.signal(123.45), 1)
        self.assertEqual(mult_escola_enzo.signal(-123.45), -1)

    def test_ten_potence(self):
        self.assertEqual(mult_escola_enzo.ten_potence(1), 1)
        self.assertEqual(mult_escola_enzo.ten_potence(10.0), 1)
        self.assertEqual(mult_escola_enzo.ten_potence(100), 1)
        self.assertEqual(mult_escola_enzo.ten_potence(0.1), 10)
        self.assertEqual(mult_escola_enzo.ten_potence(0.01), 100)
        self.assertEqual(mult_escola_enzo.ten_potence(0.001), 1000)

    def test_format_to_multiplication(self):
        function = mult_escola_enzo.format_to_multiplication
        self.assertEqual(function(11.9), 119)
        self.assertEqual(function(1234567.0), 1234567)
        self.assertEqual(function(1234567.01), 123456701)
        self.assertEqual(function(-1234567.0), 1234567)
        self.assertEqual(function(-123.0120), 123012)

    def test_mid_numbers(self):
        self.assertEqual(mult_escola_enzo.mid_numbers(98765, 12345), [493825, 3950600, 29629500,
                                                                      197530000, 987650000])
        self.assertEqual(mult_escola_enzo.mid_numbers(98765, 0), [0])
        self.assertEqual(mult_escola_enzo.mid_numbers(0, 12345), [0])
        self.assertEqual(mult_escola_enzo.mid_numbers(0, 0), [0])

    def test_mid_operation(self):
        first_result = {'signal': 1,
                        'ten_potence': 1,
                        'mid_numbers': [493825, 3950600, 29629500,
                                        197530000, 987650000]}
        second_result = {key: first_result[key] for key in first_result}
        second_result['signal'] = -1

        third_result = {key: first_result[key] for key in first_result}
        third_result['ten_potence'] = 100

        fourth_result = {key: second_result[key] for key in second_result}
        fourth_result['ten_potence'] = 1000

        self.assertEqual(mult_escola_enzo.mid_operation(98765, 12345), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-98765, -12345), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-98765, 12345), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation(98765, -12345), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation(9876.5, 1234.5), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation(987.65, 12345), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation(98765, 123.45), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-987.65, 1234.5), fourth_result)
        self.assertEqual(mult_escola_enzo.mid_operation(-98.765, 12345), fourth_result)
        self.assertEqual(mult_escola_enzo.mid_operation(98765, -12.345), fourth_result)

        self.assertEqual(mult_escola_enzo.mid_operation('98765', '12345'), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-98765', '-12345'), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-98765', '12345'), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation('98765', '-12345'), second_result)
        self.assertEqual(mult_escola_enzo.mid_operation('9876.5', '1234.5'), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation('987.65', '12345'), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation('98765', '123.45'), third_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-987.65', '1234.5'), fourth_result)
        self.assertEqual(mult_escola_enzo.mid_operation('-98.765', '12345'), fourth_result)
        self.assertEqual(mult_escola_enzo.mid_operation('98765', '-12.345'), fourth_result)

        self.assertEqual(mult_escola_enzo.mid_operation(0, 0),
                         {'signal': 1, 'ten_potence': 1, 'mid_numbers': [0]})

    def test_final_sum(self):
        first_input = {'signal': 1,
                       'ten_potence': 1,
                       'mid_numbers': [493825, 3950600, 29629500,
                                       197530000, 987650000]}
        second_input = {key: first_input[key] for key in first_input}
        second_input['signal'] = -1

        third_input = {key: second_input[key] for key in second_input}
        third_input['ten_potence'] = 100

        fourth_input = {'signal': 1, 'ten_potence': 1, 'mid_numbers': [0]}
        fifth_input = {'signal': -1, 'ten_potence': 10000, 'mid_numbers': [0]}

        self.assertEqual(mult_escola_enzo.final_sum(first_input), 1219253925)
        self.assertEqual(mult_escola_enzo.final_sum(second_input), -1219253925)
        self.assertEqual(mult_escola_enzo.final_sum(third_input), -12192539.25)
        self.assertEqual(mult_escola_enzo.final_sum(fourth_input), 0)
        self.assertEqual(mult_escola_enzo.final_sum(fifth_input), 0)

    def test_school_multiplication(self):
        self.assertEqual(mult_escola_enzo.school_multiplication(98765, 12345), 1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(987.65, 1234.5), 1219253.925)
        self.assertEqual(mult_escola_enzo.school_multiplication(-98765, 12345), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(987.65, -1.2345), -1219.253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(-98765, -12345), 1219253925)

        self.assertEqual(mult_escola_enzo.school_multiplication('98765', '12345'), 1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('987.65', '1234.5'), 1219253.925)
        self.assertEqual(mult_escola_enzo.school_multiplication('-98765', '12345'), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('987.65', '-1.2345'), -1219.253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('98765', '-12345'), -1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication('-98765', '-12345'), 1219253925)

        self.assertEqual(mult_escola_enzo.school_multiplication(0, 0), 0)

        for test in range(10):
            number_1 = randint(-10**9, 10**9)
            number_2 = randint(-10**9, 10**9)

            multiplication = float(number_1 * number_2)
            self.assertEqual(mult_escola_enzo.school_multiplication(
                number_1, number_2), multiplication)
            self.assertEqual(mult_escola_enzo.school_multiplication(
                str(number_1), str(number_2)), multiplication)


if __name__ == '__main__':
    unittest.main()
