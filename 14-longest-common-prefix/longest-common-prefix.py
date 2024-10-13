class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in strs:
            # n = len(strs[i])
            j = 0
            while j < len(i) and j < len(res):
                if  res[j] != i[j]:
                    break
                j += 1
            res = res[:j]

        return res
