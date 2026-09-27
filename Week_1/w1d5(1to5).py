a=eval(input('Enter the number: '))
if(a>0):
  print('positive')
else:
  print('negative')
  
b=35
if(a%2==0):
  print('Even')
else:
  print('Odd')  
  
c=10
d=20
e=30
print(max(c,d,e))
f=18
g=10
h=45
if(f>=g and f>=h):
  print('f is greater',f)
elif(g>=f and g>=h):
  print('g is greater',g)
else:
  print(h, 'is greater')
  
student_marks=int(input('Enter the marks of student:'))
if(student_marks<35):
  print('fail')
elif(student_marks>=35 and student_marks<50):
  print('Grade E')
elif(student_marks>=50 and student_marks<60):
  print('Grade D')
elif(student_marks>=60 and student_marks<70):
  print('Grade C')
elif(student_marks>=70 and student_marks<80):
  print('Grade B')
elif(student_marks>=80 and student_marks<90):
  print('Grade A')
elif(student_marks>=90 and student_marks<100):
  print('Grade S')
else:
  print('absent')

year=2026
if(year%4==0 and year%100!=0) or (year%400==0):
  print(year, 'is a leap year...')
else:
  print(year, 'is not a leap year...')
  
