class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n <= 3) {
            return *max_element(nums.begin(), nums.end());
        }

        int rob1 = 0, rob2 = 0, curr;
        for (int i = 0; i < n-1; i++) {
            curr = max(rob1 + nums[i], rob2);
            rob1 = rob2;
            rob2 = curr;
        }
        int firstHouse = rob2;
        rob1 = 0;
        rob2 = 0;
        for (int j = 1; j < n; j++) {
            curr = max(rob1 + nums[j], rob2);
            rob1 = rob2;
            rob2 = curr;
        }
        return max(firstHouse, rob2);
    }
};