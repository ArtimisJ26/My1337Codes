class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) == len(haystack):
        #     if needle == haystack:
        #         return 0
        #     else:
        #         return -1
        k = len(needle)
        i = 0
        while i+k <= len(haystack):
            if haystack[i:i+k] == needle:
                return i
            i += 1
        return -1