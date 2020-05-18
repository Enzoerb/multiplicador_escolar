# multiplicador_escolar

## mult_escola_enzo.py
multiply numbers in the school way

ex:  

<pre>
      98765
    x 12345
------------
     493825
   +395060
  +296295
 +197530
 +98765
-----------
 1219253925
</pre>

### signal
get the signal of a number

ex:
<pre>
>>> signal(98765)
1
>>> signal(-98765)
-1
>>> signal(0)
1
</pre>

### ten_potence
returns a multiple of ten that when multiplied by the number removes it's decimal part
ex:
<pre>
>>> ten_potence(987.65)
100
>>> ten_potence(9.8765)
10000
>>> ten_potence(0)
1
</pre>

### format_to_multiplication
removes the points of a number
ex:
<pre>
>>> format_to_multiplication(12345.0)
12345
>>> format_to_multiplication(123.45)
12345
</pre>

### mid_numbers
get the numbers you need to sum after the multiplication

ex:
<pre>
>>> mid_numbers(98765, 12345)
[493825, 395060, 296295, 197530, 98765]
</pre>

### mid_operation
excute the signal, ten_potence, format_to_multiplication and mid_numbers with all treatment required to multiply those numbers and returns a dictionary with the keys signal, ten_potence and mid_numbers

ex:
<pre>
>>> mid_operation(98765, 12345)
{
    'signal': 1,
    'ten_potence': 1,
    'mid_numbers': [493825, 395060, 296295, 197530, 98765]
}

>>> mid_operation(-9876.5, -12345)
{
    'signal': 1,
    'ten_potence': 10,
    'mid_numbers': [493825, 395060, 296295, 197530, 98765]
}

>>> mid_operation(-9876.5, 123.45)
{
    'signal': -1,
    'ten_potence': 1000,
    'mid_numbers': [493825, 395060, 296295, 197530, 98765]
}
</pre>

### final_sum
receives the dictionary created by mid_operation summing the nums in mid_numbers, adding the signal and dividing by the ten_potence

ex:
<pre>
>>> x = {
         'signal': -1,
         'ten_potence': 1000,
         'mid_numbers': [493825, 395060, 296295, 197530, 98765]
        }
>>> final_sum(x)
-1219253.925
</pre>

### school_multiplication
send the numbers to mid_operation and then the dictionary that it returns to final_sum, returning final_sum result

ex:
<pre>
>>> school_multiplication(98765, 12345)
1219253925
</pre>

## test_mult_escola_enzo.py
uses unittest to make sure that all mult_escola_enzo's functions are working properly
