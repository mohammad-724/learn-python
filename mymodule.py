def greet(name):
  return "hello, "+name+" this is my custom module"


def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return 'np'
      break
  else:
    return 'p'