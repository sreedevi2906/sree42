Open In Colab
1.write a python program to create a tuple.

In [1]:
t=(3,6,9,12)
print(t)
(3, 6, 9, 12)
In [2]:
t1=9,8,7,6
t1
Out[2]:
(9, 8, 7, 6)
2.write a python program to create a tuple with different datatypes

In [3]:
t2=(4)
print(t2,type(t2))
4 <class 'int'>
In [4]:
t2=tuple("Banglore")
print(t2,type(t2))
('B', 'a', 'n', 'g', 'l', 'o', 'r', 'e') <class 'tuple'>
In [5]:
t2=input("myself charitha")
print(type(t2))
myself charithaHow are you
<class 'str'>
In [6]:
t2=({"anantapur":1})
print(type(t2))
<class 'dict'>
In [8]:
t2=({3})
print(type(t2))
<class 'set'>
In [9]:
t2=([3.5])
print(type(t2))
<class 'list'>
3.write a python program to convert a tuple to string

In [19]:
tuple=('d','a','d')
''.join(tuple)
Out[19]:
'dad'
4.write a python program to slice a tuple.

In [30]:
t3=('hello')
t3[0:2]
Out[30]:
'he'
In [31]:
t3=(1,2,3,4,5,6,7,8,9)
slice=t3[2:5]
print(slice)
(3, 4, 5)
In [96]:
t3=(1,2,3,4,5)
t3=t3[:2]+t3[3:]
print(t3)
(1, 2, 4, 5)
5.write a python program to find the len of the tuple.

In [32]:
t4=("Cherry","Indhu","dheeru")
len(t4)
Out[32]:
3
6.write a python program to convert a tuple to a dictionary.

In [40]:
t=((1,"mom"),(2,"dad"))
print(dict((y,x) for x,y in t))
{'mom': 1, 'dad': 2}
7.write a python program to reverse a tuple.

In [41]:
t=(1,2,3,4,5,6)
t[::-1]
Out[41]:
(6, 5, 4, 3, 2, 1)
In [42]:
t=("I love you Mom")
t[::-1]
Out[42]:
'moM uoy evol I'
8.write a python program to convert a list of tuples in dictionary.

In [91]:
print (dict([('bhumika', 10), ('reetu', 7), ('aishwarya', 18), ('gowtami', 45)]))
{'bhumika': 10, 'reetu': 7, 'aishwarya': 18, 'gowtami': 45}
9.write a python program to convert a list to a tuple.

In [95]:
def convert(list):
  return (*list, )
list = [1, 2, 3, 4] 
print(convert(list))
(1, 2, 3, 4)