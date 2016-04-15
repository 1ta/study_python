ops = ['*','+','-','/']

def perm(ops, pre):
    if len(pre) == 3:
        return [pre]
    out = []
    for n in ops:
        new_pre = pre.copy()
        new_pre.append(n)
        result = perm(ops, new_pre)
        out.extend(result)
    return out

all_sort = perm(ops,[])
print(all_sort)
#print(len(all_sort))
