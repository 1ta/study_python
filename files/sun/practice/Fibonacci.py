def fab(n):
  if n==1:
    return 0
  if n==2:
    return 1
  else:
    result=fab(n-1)+fab(n-2)
    return result

print(fab(10))
