src=open('samp.txt','r')
des=open('sam.txt','w')
c=src.read()
des.write(c)
src.close()
des.close()
print('file copied successfully')

file=open('sampu.txt','r')
c=file.read()
file.close()
c=c.replace("content",'kontant')
file=open('sampu.txt','w')
file.write(c)
file.close()
print("Word replaced successfully.")

word=input("enter he word, whose line is to be printed..")
file=open('s.txt','r')
for line in file:
  if word in file:
    print(line.strip())
file.close()
print(line)



import csv
total=0
file=open('marks.csv','r')
reader = csv.reader(file)
next(reader)   # Skip header
for row in reader:
    total += int(row[1])
file.close()
print("Sum of Marks:", total)