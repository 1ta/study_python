class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        if not string: return string
        s = ''
        for i in string:
            s += i
        s = s.replace(' ','%20')
        while len(string): string.pop()
        for i in s:
            string.append(i)
        return len(s)
