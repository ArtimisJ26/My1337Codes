class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() < 1) return 0;

        sort(nums.begin(), nums.end());
        
        int res = 1, consecutive = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i-1] + 1) {
                consecutive++;
            } else if (nums[i] == nums[i-1]) {
                continue;
            } else {
                res = max(res, consecutive);
                consecutive = 1;
            }
        }
        res = max(res, consecutive);
        return res;
    }
};