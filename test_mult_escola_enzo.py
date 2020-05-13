import unittest
import mult_escola_enzo


class TestMultEscola(unittest.TestCase):

    def test_mid_operation(self):
        first_result = ['493825', '395060'+(' '*1),
                        '296295'+(' '*2), '197530'+(' '*3), '98765'+(' '*4)]
        self.assertEqual(mult_escola_enzo.mid_operation(98765, 12345), first_result)
        self.assertEqual(mult_escola_enzo.mid_operation(0, 0), ['0'])

    def test_final_sum(self):
        first_input = ['493825', '395060'+(' '*1),
                       '296295'+(' '*2), '197530'+(' '*3), '98765'+(' '*4)]
        self.assertEqual(mult_escola_enzo.final_sum(first_input), 1219253925)
        self.assertEqual(mult_escola_enzo.final_sum(['0']), 0)

    def test_school_multiplication(self):
        self.assertEqual(mult_escola_enzo.school_multiplication(98765, 12345), 1219253925)
        self.assertEqual(mult_escola_enzo.school_multiplication(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
