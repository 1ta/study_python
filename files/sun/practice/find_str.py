class Solution:
    def strStr(self, source, target):
        # write your code here
        if not isinstance(source,str) or not isinstance(target,str):
            return -1
        return source.find(target)

s = Solution()
print(s.strStr("source", ""))
print(s.strStr("abcdabcdefg", "bcd"))
print(s.strStr(35, "target"))
print(type("abcdabcdefg"))
print(type(387))
