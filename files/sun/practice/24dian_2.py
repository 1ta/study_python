
def input_four_integer():
    l = []
    nums = input("Enter 4 numbers(split with common):")
    for num in nums.split(","):
        l.append(int(num))
    return l

def perm_shuzi(arr, pre):
    if len(arr) == 0:
        return [pre]
    out = []
    for n in arr:
        new_arr = arr.copy()
        new_arr.remove(n)
        new_pre = pre.copy()
        new_pre.append(n)
        result = perm_shuzi(new_arr, new_pre)
        out.extend(result)
    return out

def perm_3_ops(ops, pre):
    if len(pre) == 3:
        return [pre]
    out = []
    for n in ops:
        new_pre = pre.copy()
        new_pre.append(n)
        result = perm_3_ops(ops, new_pre)
        out.extend(result)
    return out

def operate(a,op,b):
    if op == '/' and b==0:
        return None
    return eval(str(a) + op + str(b))

def result_24_1(num, op):
    result = operate(num[0], op[0], num[1])
    if not result is None:
        result = operate(result, op[1], num[2])
        if not result is None:
            result = operate(result, op[2], num[3])
    return result == 24.0
    
def result_24_2(num, op):
    result = 0
    result_1 = operate(num[0], op[0], num[1])
    result_2 = operate(num[2], op[2], num[3])
    if not result_1 is None and not result_2 is None:
        result = operate(result_1, op[1], result_2)
    return result == 24.0

def print_expr_1(n, o):
    return "((%d %s %d) %s %d) %s %d = 24"%(n[0], o[0], n[1], o[1], n[2], o[2], n[3])
def print_expr_2(n, o):
    return "(%d %s %d) %s (%d %s %d) = 24"%(n[0], o[0], n[1], o[1], n[2], o[2], n[3])

def calculate_all(nums, ops):
    all_ok = []
    for num in nums:
        for op in ops:
            if result_24_1(num, op):
                all_ok.append(print_expr_1(num, op))
            if result_24_2(num, op):
                all_ok.append(print_expr_2(num, op))
    return all_ok


ops = ['*','+','-','/']
all_ops = perm_3_ops(ops,[])

def one_time(input_nums):
    all_pai_lie = perm_shuzi(input_nums, [])
    ans = calculate_all(all_pai_lie, all_ops)
    for an in ans: print(an)
    print(len(ans))

def looper():
    while(True):
        try:
            input_nums = input_four_integer()
            if len(input_nums) != 4:
                break
            one_time(input_nums)
        except Exception as e:
            print(e)
            print("input error. bye!")
            break


looper()
