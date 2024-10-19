
def paths(m,n):
  if n==1 and m==1:
      return 1

  if n-1>=1 and m-1>=1:
      return paths(m-1,n)+paths(m,n-1)

  elif n-1>=1:
      return paths(m,n-1)

  elif m-1>=1:
      return paths(m-1,n)



print(paths(1,3),paths(2,4),paths(3,3))
