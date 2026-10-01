def message(func):
  def wrapper():
    print('func started')
    func()
    print('func ended')
  return wrapper
@message
def greet():
  print('Hello, Ali')
greet()

with open('samp.txt','r') as file:
  c=file.read()
  print(c)
  print('file opened')
  
