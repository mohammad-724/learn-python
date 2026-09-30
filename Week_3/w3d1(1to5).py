file=open('samp.txt','w')
for i in range(1,11):
  file.write("content written\n")
file.close()

file=open('samp.txt','r')
x=file.read()
print(x)
file.close()

file=open('samp.txt','r')
c=file.read()
y=c.split()
print(len(y))

file=open('samp.txt','r')
z=file.readlines()
print(len(z))

file=open('samp.txt','a')
a=file.write('This is a new line\n')
file=open('samp.txt','r')
q=file.read()
print(q)
file.close()