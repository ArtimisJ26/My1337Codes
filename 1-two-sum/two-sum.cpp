class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Declare Hashmap
        unordered_map<int, int> m;
        // Find if (number - target) exists in the hashmap
        for (int i = 0; i < nums.size(); i++) {
            if (m.count(target - nums[i])) {
                return {i, m[target - nums[i]]};
            }
            // Store index value pair in hashmap
            m[nums[i]] = i;
        }
        return {};
    }
};