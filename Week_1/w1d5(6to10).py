age=19
if(age>=18):
  print('Eligible to vote..')
else:
  print('Not eligible to vote..')
  
num=16
if(num%3==0):
  print(num, 'is divisible by 3')
elif(num%5==0):
  print(num, 'is divisible by 5')
else:
  print(num, 'is not divisible by 3 and 5...')
  
stu_marks=int(input('Enter the marks: '))
if(stu_marks<40):
  print('Fail')
if(stu_marks>=40 and stu_marks<50):
  print('Pass. Grade: E')
if(stu_marks>=50 and stu_marks<60):
  print('Pass. Grade: D')
if(stu_marks>=60 and stu_marks<70):
  print('Pass. Grade: C')
if(stu_marks>=70 and stu_marks<80):
  print('Pass. Grade: B')
if(stu_marks>=80 and stu_marks<100):
  print('Pass. Grade: A')
else:
  print('Invalid or absent!')
  
letter='i'
if(letter in 'aeiou'):
  print(letter, 'is a vowel')
else:
  print(letter, 'is a consonant')
  
num1=45
num2=99
result='num1 is greater' if num1>num2 else 'num2 is greater or equal to num1'
print(result)