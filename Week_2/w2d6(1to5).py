square=lambda x: x*x
num=5
print('square: ',square(num))

lists=['ali','mvgr','ece','vzm']
string='ali'
print(string.upper())
print([list1.upper() for list1 in lists])
print('---using map() function---')
upper_lists=list(map(str.upper,lists))
print(upper_lists)

n=0
for i in range(1,11):
  cubes=i**3
  print(cubes)