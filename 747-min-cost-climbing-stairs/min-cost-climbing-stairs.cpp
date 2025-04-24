class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if (cost.size() < 3) return *min_element(cost.begin(), cost.end());
        int n = cost.size();
        int next1 = cost[n-2], next2 = cost[n-1], currCost;

        for (int i = n-3; i >= 0; i--) {
            currCost = cost[i] + min(next1, next2);
            next2 = next1;
            next1 = currCost;
        }
        return min(next1, next2);
    }
};

// 10 - 1
// 9 - 100
// 8 - curr + min(8+1, 8+2) = 2
// 7 - curr + min(7+1, 7+2) = 3