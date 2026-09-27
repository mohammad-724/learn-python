print('printing 1 to 10 numbers')
for i in range(1,11):
  print(i)

print('printing even numbers between 1 to 20')  
for j in range(1,21):
  if j%2==0:
    print(j)
  if(j%2!=0):
    print(j, 'odd')

print('printing sum of first 50 numbers')
sum=0    
for k in range(1,51):
  sum+=k
print(sum)

print('factorial of a number')
n=int(input('Enter the number: '))
fact=1
for l in range(1,n+1):
  fact*=l
print('factorial of ' ,n, 'is' ,fact)

print('Multiplication table')
num=int(input('Enter the number: '))
x=0
for i in range(1,11):
  x=num*i
  print(num,'*',i,'=',x)