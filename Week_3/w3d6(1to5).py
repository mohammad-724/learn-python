import re
s='azmath'
if (re.match('^[AEIOUaeiou]',s)):
  print('string start swith vowel')
else:
  print('doesnt starts with vowel')
  
import re
n='alimohammad45'
if(re.search('[1234567890]$',n)):
  print('str ends with num')
else:
  print('doesnt ends with num')
  
import re
text='pls contact through aliazmhmd45@gmail.com or azmathalimohammad724@gmail.com or alimohammad5634t@gmail.com '
emails=re.findall(r'\S+@\S+.\S+',text)
print('Email addresses:')
print(emails)

s='azmath ali mohammad'
# print(s.replace(' ','_'))
print(re.sub(' ','_',s))

st='azmath6ali3mohammad8'
nums=re.findall(r'\d',st)
print(nums)
  