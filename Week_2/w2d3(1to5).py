dic={
  'Name':'Azmath Ali',
  'Age':20,
  'Dept':'ECE',
  'Regd_No':'23331A04B0'
}
print(dic)
print(type(dic))

print(dic.get('Name'))

x=dic['Name']='Mohammad'
print(x)
print(dic)
dic.update({'Name':'Mohammd','Age':21})
print(dic)

dic2={
  'Name':'Loki',
  'CGPA':7.83,
  'Semester':'VI'
}
print(dic2)
dic.update(dic2)
print(dic)

x=dic.popitem()
print(x)
print(dic)

