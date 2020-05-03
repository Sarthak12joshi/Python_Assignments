def prime_in_range(a,b):
  if a < 0:
    yield 'Number should be greater then 0'
  elif b < a :
    yield 'Second number should be greater then first'
  elif a > 0 and b > a:
    
    for i in range(a,b+1):
      count = 0
      for k in range(2,i):
        if i % k ==0 : 
          count = count + 1
      if count == 0:
        yield i
 
for i in prime_in_range(5,20):
  print(i)
