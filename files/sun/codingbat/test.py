
def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n ==15 or n==16:
            return n
        if 13<=n<=19:
            return 0
        else:
            return n
    sum =   fix_teen(a)+ fix_teen(b)+ fix_teen(c)
    return sum

def round_sum(a, b, c):
    def round10(num):
        if num%10<5:
            return num/10 * 10
        else:
            return (num/10+1)*10
    sum = round10(a)+round10(b)+round10(c)
    return sum

def close_far(a, b, c):
    def is_close(x):
        return abs(x-a)<=1
    def is_far(x, y1, y2):
        return abs(x-y1)>=2 and abs(x-y2)>=2
    def haha(x,y):
        return is_close(x) and is_far(y, x, a)
    return haha(b,c) or haha(c,b)
