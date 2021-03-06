# multiplicador_escolar

## mult_escola_enzo.py
multiply numbers in the school way

ex:  

<pre>
        98765
x       12345
--------------
      +493825
     +395060
    +296295  
   +197530   
  +98765    
--------------
 +1219253925
</pre>

<hr/>

### SchoolMult class

<hr/>

#### instance variables
SchoolMult class has 6 instance variables not including generated by property decorated functions.

The instance variables are:

##### multiplicador(str)
_number that will be multiplied by multiplicando(0 by default)_

##### multiplicando(str)
_number that will be multiplied by multiplicador(0 by default)_

##### mid_numbers(list of str)
_list of numbers to sum or subtract after multiplication_

ex (multiplicando = 111 and multiplicador = 11):
<pre>
>>> Mult.mid_numbers
['111', '111']
</pre>

##### result_signal(int)
_signal after multiplication_

##### potence(int)
_number of decimal places_

##### mid_sum(str)
_sum of mid_numbers without signal and point_

##### result(str)
_multiplication result_

<hr/>

#### porperty functions
SchoolMult class has 2 property functions

The property functions are:

##### higher_number -> str:
_returns higher number between multiplicador and multiplicando_

##### lower_number -> str:
_returns lower number between multiplicador and multiplicando_

<hr/>

#### staticmethods
SchoolMult class has 1 staticmethod

##### potence_format
_given a numerical string it returns the string without point and how many decimal places it had_

ex:
<pre>
>>> Mult = SchoolMult()
>>> Mult.potence_format('12345')
('12345', 0)
>>> Mult.potence_format('123.45')
('12345', 2)
>>> Mult.potence_format('0.012345')
('0012345', 6)
</pre>

<hr/>

#### instance methods

##### signal
get the result signal and saves in the instance variable result_signal

ex:
<pre>
>>> Mult = SchoolMult('123', '123')
>>> Mult.signal()
>>> Mult.result_signal
1

>>> Mult = SchoolMult('123', '-123')
>>> Mult.signal()
>>> Mult.result_signal
-1

>>> Mult = SchoolMult('-123', '-123')
>>> Mult.signal()
>>> Mult.result_signal
1
</pre>

##### ten_potence
gets the number of decimal cases and saves in the instance variable potence

ex:
<pre>
>>> Mult = SchoolMult('123', '123')
>>> Mult.ten_potence()
>>> Mult.potence
0

>>> Mult = SchoolMult('1.23', '123')
>>> Mult.ten_potence()
>>> Mult.potence
2

>>> Mult = SchoolMult('12.3', '1.23')
>>> Mult.ten_potence()
>>> Mult.potence
3
</pre>


##### mid_operation
get the numbers you need to sum or subtract after the multiplication saving it in the instance variable mid_numbers

ex:
<pre>
>>> Mult = SchoolMult('12.3', '1.23')
>>> Mult.mid_operation()
>>> Mult.mid_numbers
['369', '246', '123']

>>> Mult = SchoolMult('123', '123')
>>> Mult.mid_operation()
>>> Mult.mid_numbers
['369', '246', '123']

>>> Mult = SchoolMult('11', '-111')
>>> Mult.mid_operation()
>>> Mult.mid_numbers
['111', '111']
</pre>


##### final_sum
sum numbers in the instance variable mid_numbers saving the result in self.mid_sum. After it adds the signal and decimal places, saving the output in self.result


ex:
<pre>
>>> Mult = SchoolMult('12.3', '1.23')
>>> Mult.mid_operation()
>>> Mult.signal()
>>> Mult.ten_potence()
>>> Mult.final_sum()
>>> Mult.mid_sum
15129
>>> Mult.result
+15.129

>>> Mult = SchoolMult('123', '123')
>>> Mult.mid_operation()
>>> Mult.signal()
>>> Mult.ten_potence()
>>> Mult.final_sum()
>>> Mult.mid_sum
15129
>>> Mult.result
+15129

>>> Mult = SchoolMult('11', '-111')
>>> Mult.mid_operation()
>>> Mult.signal()
>>> Mult.ten_potence()
>>> Mult.final_sum()
>>> Mult.mid_sum
1221
>>> Mult.result
-1221
</pre>

##### include_decimal
given a number and the number of spaces returns the number with the point and right spaces included

ex:

<pre>
>>> Mult = SchoolMult()
>>> Mult.potence = 3
>>> print( Mult.include_decimal('1234', 4) + '.' )
1.234    .
</pre>
_period printed to show and of spaces_

##### include_signal
include number signal

ex:

<pre>
>>> Mult = SchoolMult()
>>> Mult.result_signal = -1
>>> print( Mult.include_signal('1234'))
-1234
</pre>

##### format_number_str
runs include_decimal, include_signal and add left spaces in a number.
The number of left spaces is len(self)-len(number) and the number of right spaces(when runing include_decimal) is a function attribute

ex:

<pre>
>>> Mult = SchoolMult()
>>> Mult.result = +1234567.89
>>> Mult.potence = 3
>>> Mult.result_signal = -1
>>> print( Mult.format_number_str('1234', 2) + '.')
   -1234  .
</pre>
_period printed to show and of spaces_

<hr/>

#### Magic/Dunder Methods

##### len
returns the len of self.result

ex:

<pre>
>>> Mult = SchoolMult('12345', '98765')
>>> Mult.mid_operation()
>>> Mult.signal()
>>> Mult.ten_potence()
>>> Mult.final_sum()
>>> print(len(Mult))
11
</pre>

##### str
returns the visual format of the multiplication

ex:

<pre>
>>> Mult = SchoolMult('12345', '98765')
>>> Mult.mid_operation()
>>> Mult.signal()
>>> Mult.ten_potence()
>>> Mult.final_sum()
>>> print(str(Mult))
        98765
x       12345
--------------
      +493825
     +395060
   +296295  
  +197530   
  +98765    
--------------
 +1219253925
</pre>

<hr/>

## test_mult_escola_enzo.py
uses unittest to make sure that all mult_escola_enzo's functions are working properly
