def more(c, ar=None):
    if ar is None:
        return more(c-1, [0,1,2,3,4,5,6,7,8,9])
    if c == 0:
        return ar
    oar = []
    for a in ar:
        for i in range(10):
            oar.append(int(str(a) + str(i)))
    return more(c-1, oar)
# arr = more(n)
# if len(arr) > 0:
#     arr.remove(0)
# return arr

print(more(2))
