class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        new_len = length
        if string == None:
            return None
        for str_1 in string:
            if str_1 == " ":
                new_len += 2
        for i in range(new_len):
            if string[i] == " ":
                string.remove(" ")
                string.insert(i,'0')
                string.insert(i,'2')
                string.insert(i,'%')
        return new_len
