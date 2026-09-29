###num=int(input('Enter the number: '))
#if(num<=1):
#  print('Not a prime')
#else:
#  for i in range(2,num):
#    if num%i==0:
#      print('Not prime')
#      break
#  else:
#    print('Prime number')
    
n=5
if n<=1:
  print('not prime')
else:
  for i in range(2,n):
    if n%i==0:
      print('not prime')
      break
  else:
    print(' prime')
    
def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return 'not prime'
      break
  else:
    return 'prime'
n=11
print(is_prime(n))  

    
def is_prime(num):
  if num<=1:
    return False
  for i in range(2,num):
    if num%i==0:
      return False
  return True  
n=int(input('enter num: '))
if is_prime(n):
  print('Prime')
else:
  print('Not prime')
  
#n=5
#fact=1
#for i in range(1,n+1):
#  fact*=i
#print(fact)

def factorial(digit):
  fact=1
  for i in range(1,digit+1):
    fact=fact*i
  return fact
x=int(input('ENter number: '))
result=factorial(x)
print(result)

def is_pal(string):
  if s==s[::-1]:
    return True
  return False
s='ali'
if is_pal(s):
  print('palindrome')
else:
  print('not palindrome')
  
def fibonacci(y):
  if y<=1:
    return y 
  else:
    return fibonacci(y-1)+fibonacci(y-2)
y=int(input('Enter num of terms:'))
print('Fibonacci series')
for i in range(y):
  print(fibonacci(i), end=" ")
  
def list_sum(numbers):
  total=0
  for i in numbers:
    total+=i
  return total
lst=[10,20,30,40,60]
print(list_sum(lst))

print(sum(lst))




def is_prime(n):
  if n<=1:
    return False
  for i in range(2,n):
    if n%i==0:
      return False
  return True
num=int(input('Enter num'))
if is_prime(num):
  print('Prime')
else:
  print('NOt prime')

def factorial(x):
  fact=1
  for i in range(1,x+1):
    fact=fact*i
  return fact
y=5
result=factorial(y)
print(result)

def is_pal(string):
  if string==string[::-1]:
    return True
  return False
string='mala'
if is_pal(string):
  print('pal')
else:
  print('mot pal')
  
def fibonacci(n):
  a=0
  b=1
  for i in range(n):
    print(a ,end=" ")
    c=a+b
    a=b
    b=c
n=10
print('Fibonacci Sequence is: ',fibonacci(n))

def sum(list):
  total=0
  for i in list:
    total+=i
  return total
list=[10,20,30,40,50]
print(sum(list))