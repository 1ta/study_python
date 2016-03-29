def double_char(str):
    b=""
    for i in range(len(str)):
        return b=i*2

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
    return str.count("cat")==str.count("dog")

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      count += 1
  return count

def end_other(a, b):
    s1 = str.lower(a)
    s2 = str.lower(b)
    suffix_1 = s1[-4:]
    suffix_2 = s2[-4:]
    return s1.endswith(suffix_2) or s2.endswith(suffix_1)

def xyz_there(str):
    #a = str.count("xyz")
    #b = str.count(".xyz")
    #return a>b
    if str[:3] == "xyz":
        return True
    for i in range(len(str)-3):
        if str[i] != "." and str[i+1 : i+4] == "xyz":
            return True
    return False
