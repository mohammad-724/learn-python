my_list=[1,2,1,1,3,2,4,4,2,3,6,5,5,3,6,7,2,4]
print(my_list)
my_set=set(my_list)
print(my_set)

set1={10,20}
set2={10,20,30,40,50}
print(set1.issubset(set2))
print(set1.issuperset(set2))

print(set1.symmetric_difference(set2))

my_frozen_set = frozenset(["Mercury", "Venus", "Earth", "Mars"])
print(f"Content: {my_frozen_set}")
print(f"Type: {type(my_frozen_set)}")
try:
    my_frozen_set.add("Jupiter")
except AttributeError as e:
    print(f"Error: {e}")
    
set3={11,12,13,14,15}
set4={11,12,13,14,15,16,17,18,19,20}
x=set3.issubset(set4)
print(x)