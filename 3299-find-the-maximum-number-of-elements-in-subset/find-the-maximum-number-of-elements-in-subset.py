class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        maxSubset = 1
        # [1,3,4,5,6,7,9]
        # -> [x, x2, x4,]
        # sort, check if its duplicate exists, if yes, then check if its square exists(recursively)
        # [5,4,1,2,2]
        arr = set(sorted(nums))
        print(arr)
        # [1,2,2,4,5]
        def findSubset(i, count):
            print(i,count)
            if i not in arr:
                return count-1
            if nums.count(i) < 2:
                return count+1
            
            if i != 1:
                print("->",i,count)
                count = findSubset(i**2, count+2)
            return count

        for i in arr:
            if i < 10**5:
                if i == 1:
                    count = nums.count(i)
                    if count % 2 == 0:
                        count -= 1
                else:
                    count = findSubset(i,0)
                # print(count)
                maxSubset = max(maxSubset,count)

        return maxSubset