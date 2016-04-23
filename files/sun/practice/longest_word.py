class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        def word_len_list(dictionary):
            wd_list =[]
            for word in dictionary:
                wd_list.append(len(word))
            return max(wd_list)

        def find_word(dictionary):
            result = []
            for word in dictionary:
                if len(word) == word_len_list(dictionary):
                    result.append(word)
            return result
        return find_word(dictionary)

print(Solution().longestWords(["apped","apdoap","pajdnd","adjdnd"]))
