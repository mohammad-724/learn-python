import re
phone=input('Enter phn number: ')
if re.fullmatch(r'[6-9]\d{9}',phone):
  print('valid phnh number')
else:
  print('invalid phn number')
  
import re
s='azmath ali mhmd'
print(re.split(r'\s+',s))

import re
t='ali mohammad azmath ali ali ali mohammad '
result=re.findall(r'\b(\w+)\s+\1\b',t)
print(result)

import re
u='Hello@Python$Programmi*ng#123'
x=re.sub(r'[^A-Za-z0-9]','',u)
print(x)

v='My birthday is 20/08/2005 and ecam is on 25/07/2026'
dates=re.findall(r'\d{2}/\d{2}/\d{4}',v)
print("Dates: ",dates)