def make_tags(tag, word):
  return "<%s>%s</%s>"%(tag,word,tag)

def make_out_word(out, word):
    return out[:2]+word+out[-2:]

def extra_end(str):
    return str[-2:]*3

def first_two(str):
    return str[:2]

def first_half(str):
    length = len(str)/2
    return str[:length]

def without_end(str):
    return str[1:len(str)-1]

def combo_string(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a
def non_start(a, b):
    return a[1:]+b[1:]

def left2(str):
    return str[2:]+str[:2]
