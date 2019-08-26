Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2**5
32
>>> a=20
>>> b=30
>>> c=a+b
>>> c
50
>>> a=input("enter value of a;")
enter value of a;20
>>> b=input("enter value of b;")
enter value of b;30
>>> c=a+b
>>> c
'2030'
>>> int(input("enter value of a;"))
enter value of a;20
20
>>> int(nput("enter value of b;"))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    int(nput("enter value of b;"))
NameError: name 'nput' is not defined
>>> int(input("enter value of b;"))
enter value of b;30
30
>>> c=a+b
>>> int(c=a+b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int(c=a+b)
TypeError: 'c' is an invalid keyword argument for int()
>>> a="python programming"
>>> print(a.upper())
PYTHON PROGRAMMING
>>> print(a.lower())
python programming
>>> print(a.replace("python","c"))
c programming
>>> a=[1,2,3,4,8,-1,2.2,'b']
>>> a.append(5)
>>> a
[1, 2, 3, 4, 8, -1, 2.2, 'b', 5]
>>> b=[1,2,3]
>>> a.extend(['a','b'])
>>> a
[1, 2, 3, 4, 8, -1, 2.2, 'b', 5, 'a', 'b']
>>> a.extend(b)
>>> a=[1,2]
>>> b=[3,4]
>>> a.extend(b)
>>> a
[1, 2, 3, 4]
>>> a=[-1,4,5]
>>> b=[7,8,9]
>>> a+b
[-1, 4, 5, 7, 8, 9]
>>> a.index(-1)
0
>>> a=["CMR","good","college"]
>>> a.insert(1,"is")
>>> a
['CMR', 'is', 'good', 'college']
>>> a.replace("college","university")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.replace("college","university")
AttributeError: 'list' object has no attribute 'replace'
>>> a.insert(3,"university")
>>> a
['CMR', 'is', 'good', 'university', 'college']
>>> a.remove(4)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.remove(4)
ValueError: list.remove(x): x not in list
>>> a.remove(4,"college")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.remove(4,"college")
TypeError: remove() takes exactly one argument (2 given)
>>> a.remove("college",/)
SyntaxError: invalid syntax
>>> a
['CMR', 'is', 'good', 'university', 'college']
>>> a.remove("college")
>>> a
['CMR', 'is', 'good', 'university']
>>> a=[1,2,4,8,-1,2.2,'b',2,2]
>>> a.count(2)
3
>>> a=[1,2,3]
>>> a[0;2]
SyntaxError: invalid syntax
>>> a[0:2]
[1, 2]
>>> a=(1,2,3,"a")
>>> a.append(5)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> a
(1, 2, 3, 'a')
>>> a*2
(1, 2, 3, 'a', 1, 2, 3, 'a')
>>> 
