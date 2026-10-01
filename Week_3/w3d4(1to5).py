l=[10,20,30,40,50]
it=iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print('iteration using for loop')
f=['apple','banana','mango']
for i in f:
  print(i,sep=',')
  
def squares():
  for i in range(1,11):
    yield i**2
for x in squares():
  print(x)
  
def even():
  for i in range(1,51):
    if i%2==0:
      yield i
for x in even():
  print(x)
  
n=8
a=0
b=1
for i in range(1,n-1):
  c=a+b
  a=b
  b=c
  print(a)

print('fibonacci using generators')
def fib(n):
  a=0
  b=1
  for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    yield a
for x in fib(10):
  print(x)