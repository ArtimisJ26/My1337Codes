class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> result;
        int n = nums.size();
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n; i++) {
            int firstDiff = 0-nums[i];
            int l = i+1, r = n-1;
            while (l < r) {
                if (nums[l] + nums[r] == firstDiff) result.insert({nums[i], nums[l], nums[r]});
                if (nums[l] + nums[r] > firstDiff) r--;
                else {l++;}
            }
        }
        vector<vector<int>> final(result.begin(), result.end());
        
        return final;
    }
};
