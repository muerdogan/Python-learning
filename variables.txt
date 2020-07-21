Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #variables
>>> 
>>> type(12)
<class 'int'>
>>> 

>>> type(8.7)
<class 'float'>
>>> type("python")
<class 'str'>
>>> type('3')
<class 'str'>
>>> type([1,1,2,3,5,8])
<class 'list'>
>>> type((1,2,3,4))
<class 'tuple'>
>>> type({"apple":"fruit"))
SyntaxError: invalid syntax
>>> type({"apple":"fruit"})
<class 'dict'>
>>> 
>>> 
>>> x = y = 3
>>> x + y
6
>>> z = int(3.8)
>>> z
3
>>> z2 = float(3.8)
>>> z2
3.8
>>> print(z2)
3.8
>>> type(z)
<class 'int'>
>>> type(z2)
<class 'float'>
>>> float(3)
3.0
>>> type(str(3))
<class 'str'>
>>> int("text")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    int("text")
ValueError: invalid literal for int() with base 10: 'text'
>>> float("text")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float("text")
ValueError: could not convert string to float: 'text'
>>> int("57")
57
>>> int("57x")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int("57x")
ValueError: invalid literal for int() with base 10: '57x'
>>> 
