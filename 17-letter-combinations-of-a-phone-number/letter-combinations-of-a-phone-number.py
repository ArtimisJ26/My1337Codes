class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ### Use backtracking for this problem because we need to find every possible combination
        # Result to return
        res = []
        # create a hashmap of the letters associated with each number
        digitToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"

        }
        # explore the backtracing tree down-up using recursion i=position of current digit in digits
        def dfs(i, currString):
            # declare base case
            if len(currString) == len(digits):
                res.append(currString)
                return
            # now loop ahead for the characters in the next digit
            for char in digitToChar[digits[i]]:
                # write the recursive call
                dfs(i + 1, currString + char)

        if digits:
            dfs(0,"")
        
        return res