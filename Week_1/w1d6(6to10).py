num=1234
reverse=0
while num>0:
  digit=num%10
  reverse=reverse*10+digit
  num=num//10
print('reverrsd number is',reverse)
number='4456'
z=number[::-1]
print(z)
x=int(z)
print(x)
print(type(x))

n='8501835123'
o=len(n)
print(o)
print(int(o))

a=0
b=1
y=10
for i in range(y):
  a,b=b,a+b
  print(a, end="\n ")
  
rows=5
for j in range(1,rows+1):
  for k in range(j):
    print('*',end=" ")
  print()
  
for l in range(1,11):
  if l==6:
    break
  print(l)

for l in range(1,11):
  if l==6:
    continue
  print(l)
