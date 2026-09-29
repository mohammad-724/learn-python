#nums=45,10,18
#print(max(nums))

#def maximum(nums):
#  maxim=0
#  return max(nums)
#nums=45,66,99,10,7,18
#print(max(nums))

def maximum(a,b,c):
  if a>=b and a>=c:
    return a
  elif b>=a and b>=c:
    return b
  else:
    return c
x,y,z=45,66,99
print('maaxx among 3 nums is : ',maximum(x,y,z))

def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a
x,y=12,18
print('gcd of is',gcd(x,y))  

#string='ali azmath mohammad'
#count=0
#print(string.count('a')+string.count('e')+string.count('i')+string.count('o')+string.count('u'))
#for char in string:
#  if char in 'aeiou':
#    count+=1
#print(count)

def vowels(s):
  count=0
  for char in s:
    if char.lower() in 'aeiou':
      count+=1
    return count
text='azmath ali mohammad'
print('vowels in text are: ',vowels(text))

#string3='azmath ali'
#x=string3[::-1]
#print(x)

def  str_reversal(string2):
  rev=string2[::-1]
  return rev
string3='ali mohammad'
print('reversed string is : ',str_reversal(string3)) 

num=12345
sum=0
while num>0:
  digit=num%10
  sum=sum+digit
  num=num//10
print('sum is',sum)

def sum_digits(n):
  total=0
  while n>0:
    digit=n%10
    total=total+digit
    n=n//10
  return total
num=8501835123
print('sum is : ',sum_digits(num))
  