
w_dic = {}
def word_dic(dictionary,w_dic):
    for i in dictionary:
        w_dic[i]= len(i)
    return w_dic

my_dic = {"a":1,"sc":2,"xcb":3,"dxa":3}
def val_key(dic):
    vk = []
    for key in dic:
        if(key):
            vk.append((dic[key],key))
    return vk


#print(word_dic(["acv","acvd","wertd","abcds"],{}))
#print(val_key(my_dic))
#print(val_key(my_dic)[1][1])
print(len(val_key(my_dic)))
