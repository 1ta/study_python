def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def sum_double(a, b):
  if a = b:
      return 2
  else:
      return a+b

def diff21(n):
    if n < 21:
        return(21-n)
    else:
        return(2*(n-21))

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False

def front3(str):
    if len(str)>=3:
        return str[0:3]+str[0:3]+str[0:3]
    else:
        return str+str+str
