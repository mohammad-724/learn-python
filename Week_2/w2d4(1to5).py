squares=[x**2 for x in range(1,11)]
print(squares)

even=[x for x in range(1,51) if x%2==0]
print(even)
odd=[x for x in range(1,51) if x%2!=0]
print(odd)

string='azmath ali mohammad'
vowels=[char for char in string if char.lower() in 'aeiou']
print(vowels)

l=[[1,2],
   [3,4],
   [5,6]]
print(l)
print(type(l))
l2=[y for r in l for y in r]
print('Flattened list: ',l2)

sqr={num: num**2 for num in range(1,11)}
print('Dictionary of numbers and their squares:',sqr)