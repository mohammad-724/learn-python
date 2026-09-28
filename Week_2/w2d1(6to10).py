list_1=[8,3,5,1,9,6,2,7,4]
asc_list_1=sorted(list_1)
print('Ascending order',sorted(asc_list_1))
print('Descending order ',asc_list_1[::-1])
desc_list_1=asc_list_1.reverse()
print('Descending order ',desc_list_1)

list_2=[1,5,3,3,1,8,4,2,2,6,9,7,4,1,1,1]
print(list_2)
print(list_2.count(1))

print('merging two lists',list_1+list_2)
print(sorted(list_1+list_2))

print('rotating a list')
list_3=[1,2,3,4,5]
k=2
n=len(list_3)
k=k%n
rotated_list=list_3[-k:]+list_3[:-k]
print(rotated_list)

list_4=[45,10,18,7,99]
sort=sorted(list_4)
print(sort)
desc_list_4=sort[::-1]
print(desc_list_4)
print(desc_list_4[1])