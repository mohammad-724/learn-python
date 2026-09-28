my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list)
print(type(my_list))
print('first number is ',my_list[0])
print('last number is ',my_list[-1])
print('middle number is ',my_list[4])

print(my_list[::-1])
print(my_list[1:9:2])
my_list.reverse()
print(my_list)

my_list2=[1,2,3,4,5,6,7,8,9,10]
my_list2.append(11)
print(my_list2)
my_list2.append([12,13,14,15,16])
print(my_list2)
my_list2.extend([16,17,18,19,20])
print(my_list2)

my_list3=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,7,7,8]
print(my_list3)
my_set3=set(my_list3)
print(my_set3)
print('set--> to list converted in-order to remove duplicates')
print(list(my_set3))

my_list4=[45,10,18,7]
print(max(my_list4))
print(min(my_list4))