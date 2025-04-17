class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // create vector or number and index pairs
        vector<pair<int, int>> pairs;

        for (int i = 0; i < nums.size(); i++){
            pairs.push_back({nums[i], i});
        }

        // sort the vector
        sort(pairs.begin(), pairs.end());

        // find the pair using two pointer method
        int l = 0, r = nums.size() - 1;

        while (l < r){
            int curr = pairs[l].first + pairs[r].first;
            if(curr == target) {
                return {min(pairs[l].second, pairs[r].second),
                    max(pairs[l].second, pairs[r].second)};
            } else if (curr > target) {
                r--;
            } else {
                l++;
            }
        }
        return {};
    }
};