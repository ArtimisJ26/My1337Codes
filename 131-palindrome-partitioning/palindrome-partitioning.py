class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(left):
            if left >= len(s):
                res.append(part.copy())     
                return
            for i in range(left,len(s)):
                if self.isPalindrome(s, left, i):
                    part.append(s[left:i+1])
                    dfs(i+1)
                    part.pop() 
        # res = []  # all possible partitions
        # part = [] # current partition

        # # lets trast by partitioning it from the left side
        # def dfs(left):
        #     # base case, no more characters to partition
        #     if left >= len(s):
        #         # part.copy() since "part" will change in different instances of the recursion
        #         res.append(part.copy())     
        #         return
        #     # create possibilities of partitions from the left 1chars, 2chars, 3chars
        #     for i in range(left,len(s)):
        #         # lets see if the left partition that we created is a palindrome
        #         if self.isPalindrome(s, left, i):
        #             # add it to the partition array
        #             part.append(s[left:i+1])
        #             # if yes, only then explore its further partitions
        #             dfs(i+1)
        #             # Remove the string that we just added above so that this variable can be reused in other iterations
        #             part.pop()    
                    
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        if len(s) == 1:
            return True
        
        # Two pointer to check palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True