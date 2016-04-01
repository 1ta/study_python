fp = open('./Harry Potter 1.txt', 'r')
content = fp.read()

content = content.replace(",", "").replace(".", "").replace("\"", "") \
.replace("-", "").replace("\\", "").replace("?", "").replace("!", "")

content = content.lower()

lines = content.split('\n')

words = []
for line in lines:
    words += line.split(" ")

dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

# print(dictionary)

vk_list = []
for key in dictionary:
    if(key):
        vk_list.append((dictionary[key], key))

vk_list.sort(reverse=True)
# print(vk_list)
# for c,key in vk_list:
#     if c > 50:
#         print(key, c)

output = ''
for i in range(200):
    # print(vk_list[i])
    output += "\n" + vk_list[i][1] + ' ' + str(vk_list[i][0])

print(output)
fp = open('./output.txt', 'w')
fp.write(output)
