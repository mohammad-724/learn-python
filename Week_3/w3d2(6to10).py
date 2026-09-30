try:
  a=10
  b=eval(input('enter the number: '))
  r=a/b
except ValueError:
  print('invalid value')
except ZeroDivisionError:
  print('cant divide with 0')
except KeyError:
  print('key not found')
except Exception as e:
  print('Error.',e)
else:
  print('result is: ',r)

try:
  l=[1,2,3,4,5]
  print(l[7])
except IndexError:
  print('index is out of range')
  
try:
  s='ali'
  x=int(s)
  print('str to int is',x)
except:
  print('cant convert strinfg to int')

class InValidAgeError(Exception):
  pass 
try:
  age=int(input('Enter tyhe age: '))
  if age<18:
    raise InValidAgeError('Age should be greater than 18')
  print('Eligible')
except InValidAgeError as e:
  print('invalid age..',e)
  
attempt=3
while attempt>0:
  try:
    filename=input('Enter file name: ')
    file=open(filename,'r')
    print(file.read())
    file.close()
    break
  except IOError:
    print('Error reading file. Try again..')
    attempt-=1
if attempt==0:
  print('max attempts reached')
  
attempts=3
while attempts>0:
  try:
    f=input('Enter file name')
    file=open(f,'w')
    content=file.write("this file was re-written")
    file.close()
    break
  except IOError:
    print('file not found. Try again')
    attempts-=1
if attempts==0:
  print('max limit reached')