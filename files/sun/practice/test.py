
def input_four_integer():
    l = []
    nums = input("Enter 4 numbers(split with common):")
    for num in nums.split(","):
        l.append(int(num))
    return l

def perm(arr, pre):
    if len(arr) == 0:
        return [pre]
    out = []
    for n in arr:
        new_arr = arr.copy()
        new_arr.remove(n)
        new_pre = pre.copy()
        new_pre.append(n)
        result = perm(new_arr, new_pre)
        out.extend(result)
    return out

all_sort = perm(input_four_integer(), [])
print(all_sort)

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
