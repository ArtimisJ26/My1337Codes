class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)
        ans = s[0]

        for i in range(n):
            for j in range(i,n):
                if s[i] == s[j]:
                    if s[i:j+1] == s[i:j+1][::-1] and j-i+1 > len(ans):
                        ans = s[i:j+1]

        return ans