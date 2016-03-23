def string_times(str, n):
    return str*n

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

def array_front9(nums):
    for num in nums[:4]:
        if num == 9:
            return True
    else:
        return False

def array123(nums):
    for num in nums:
        if num[i]==1 and num[i+1]==2 and num[i+2]==3:
            return ture
    return False

def string_match(a, b):
    shorter = min(len(a),len(b))
    count = 0

    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub = b_sub:
            count += 1
    return count
