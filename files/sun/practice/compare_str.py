class Solution:
    def compareStrings(self, A, B):
        def addletter(strStr,l_Dict):
            l_Dict = {}
            for l in strStr:
                if l in l_Dict:
                    l_Dict[l] += 1
                else:
                    l_Dict[l] = 1
            return l_Dict

        def compare_dic(dic_1,dic_2):
            for key in dic_2:
                if not key in dic_1.keys():
                    return False
                elif dic_1[key] < dic_2[key]:
                    return False
            return True

        def cmp_str(A,B):
            r_1 = addletter(A,{})
            r_2 = addletter(B,{})
            return compare_dic(r_1,r_2)
        return cmp_str(A, B)

print(Solution().compareStrings('ABCD', ''))
