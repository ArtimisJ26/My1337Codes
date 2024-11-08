class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        size = len(height)
        leftArr = [0] * size
        rightArr = [0] * size        
        res = 0

        leftArr[0] = height[0]
        rightArr[size-1] = height[size-1]

        for i in range(1, size):
            leftArr[i] = max(leftArr[i-1], height[i])
        
        for i in range(size - 2, -1, -1):
            rightArr[i] = max(rightArr[i+1], height[i])
        
        for i in range(1, size-1):
            res += min(leftArr[i], rightArr[i]) - height[i]

        return res