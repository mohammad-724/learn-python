try:
  a=10
  b=0
  s=a/b
  print('result is: ',s)
except ZeroDivisionError:
  print('Error: not divisible by 0')
  
try:
  f=open('s.txt','r')
  print(f.read())
  f.close()
except FileNotFoundError:
  print('file not found')
  
try:
  s='ali'
  n=1
  r=s+n
  print('added',r)
except TypeError:
  print('cant add both string and num')
  
try:
  a=10
  b=int(input('emnter the number to be divided: '))
  s=a/b
  print('result is: ',s)
except ZeroDivisionError:
  print('cant divide with zero')
else:
  print('result is',s)
finally:
  print('executed successfully')
  
num=int(input('enter the number'))
if num<=0:
  print('no negative numbers ')
else:
  print('the number is: ',num)
  
try:
  n=int(input('enter the number: '))
  if n<0:
    raise ValueError('Negatve numbers are not allowed')
  print('number=',n)
except ValueError as e:
  print('error',e) 