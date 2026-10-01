def readfiles(filename):
  with open(filename,'r') as file:
    for line in file:
      yield line.strip()
for line in readfiles('largefile.txt'):
  print(line)
  
data=iter([45,10,18,7])
for value in iter(lambda:next(data),7):
  print(value)
  
from itertools import chain
it1=['ali','loki','sarat']
it2=['apple','banana','mango']
for items in chain(it1,it2):
  print(items)
  
def prime_generator():
  for num in range(2,101):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
      if num%i==0:
        is_prime=False
        break
    if is_prime:
      yield num
for prime in prime_generator():
  print(prime)
  
def div5():
  num=5
  while True:
    yield num
    num+=5
gen=div5()
for i in range(10):
  print(next(gen))
  
      