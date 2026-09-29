string='azmath ali mohammad'
freq={char: string.count(char) for char in string}
print(freq)

uni={unq: string.count(unq) for unq in string}
print(uni)
print(set(string))
print(set(uni))

str2='electronics and communication engineering'
uniq={x for x in str2}
print(uniq)
print(set(str2))

list1=[7,10,17,18,33,45,66,99]
odd=[x for x in list1 if x%2!=0]
print(odd)


t=[(x,x**2) for x in range(1,11)]
print(t)

sentence='hii my name is mohammad azmath ali im pursuing btech currently'
words=[word for word in sentence.split() if len(word)>4]
print(words)