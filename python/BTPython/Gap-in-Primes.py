def gap(g, m, n):
    start = 0
    end = 0
    for i in range(m,n+1):
      if is_prime(i):
        if start == 0:
          start = i
        elif end == 0:
          end = i
        else:
          start = end
          end = i
      if end - start == g:
        return [start, end]
    return None




def is_prime(n):
  if n <= 0 or n == 1:
    return False
  for i in range(2,int(n**0.5+1)):
      if n%i == 0:
          return False
  return True

print(gap(10,300,400))