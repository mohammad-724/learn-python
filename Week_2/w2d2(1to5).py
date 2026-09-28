my_tuple1=(1,2,3,4,5)
print(my_tuple1)
print(type(my_tuple1))
print(len(my_tuple1))
print(my_tuple1.__len__())

my_list2=[5,6,7,8,9]
print('list',my_list2)
print('list to tuple')
my_tuple2=tuple(my_list2)
print('tuple',my_tuple2)
print('tuple to list')
my_list2a=list(my_tuple2)
print('llist',my_list2a)

print(my_tuple1.index(3))
print(my_tuple1[4])

list=[1,'ali',3]
print(list)
tuple=(1,'ali',3)
R_no,Name,Section=tuple
print(tuple)
print('R_no: ',R_no)
print('Name: ',Name)
print('Sec: ',Section)
p=tuple[1].replace('ali','azmath')
print(p)
print(tuple)

set1={10,20,30,40,50}
set2={60,70,80,90,100}
print(set1)
print(set2)
print(type(set1))
set_u=set1.union(set2)
print('union',set_u)
print(set(sorted(set_u)))
set_i=set1.intersection(set2)
print('intersection',set_i)
set_d=set1.difference(set2)
print('difference',set_d)