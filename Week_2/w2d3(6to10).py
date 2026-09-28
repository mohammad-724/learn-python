string="mohammad azmath ali"
dic={
  'name':'mohammad azmath ali',
  'age':20
}
x=dic['name'].count('a')
print(x)

dic2 = {
    "a": 1,
    "b": 3,
    "c": 2
}
inverted = {value: key for key, value in dic2.items()}
print(inverted)

print(max(dic2))

print('name' in dic)
print('name' in dic2)

dic3 = {
    "a": 3,
    "b": 1,
    "c": 2
}
z=dict(sorted(dic3.items(), key=lambda item: item[1]))
print(z)            