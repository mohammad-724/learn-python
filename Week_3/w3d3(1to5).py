import math
n=5
p=3
print('factorial is: ',math.factorial(n))
print('power cuube is : ',math.pow(n,p))

import random
for i in range(10):
  print(random.randint(1,100))
  
print(('otp pins generation'))
import random
for i in range(1):
  print(random.randint(1000,9999))
  
import random
l=[1,2,3,4,5]
print(random.choice(l))

import random
l=[10,20,30,40,50,60]
random.shuffle(l)
print(l)

import sys
print('command line arguments')
for arg in sys.argv:
  print(arg)