class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        cache = []
        maxlength = 0
        for word in dictionary:
            l = len(word)
            if l >= maxlength:
                cache = []
                maxlength = l
                cache.append(word)
            elif l == maxlength:
                cache.append(word)

        return cache


print(Solution().longestWords(["apped","apdoap","pajdnd","adjdnd"]))
