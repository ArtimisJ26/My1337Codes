class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        int step1 = 1, step2 = 2, stepNum = n - 2, curr;
        
        while (stepNum > 0) {
            curr = step1 + step2;
            step1 = step2;
            step2 = curr;
            stepNum--;
        }
        return step2;
    }
};

// 9 - 1
// 8 - 2
// 7 - (8) + (9) = 3
// 6 - (7) + (8) = 5
// 5 - (6) + (7) = 8
// 4 - (5) + (6) = 13
// 3 - (4) + (5) = 21
// 2 - (3) + (4) = 34
// 1 - (2) + (3) = 55

// 4 - 1
// 3 - 2
// 2 - 3
// 1 - 5

// 2 - 1
// 1 - 2