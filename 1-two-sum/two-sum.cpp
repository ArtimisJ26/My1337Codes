class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Declare Hashmap
        unordered_map<int, int> indices;

        // Store index value pairs in hashmap
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }
        
        // Find if (number - target) exists in the hashmap
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (indices.count(diff) && indices[diff] != i) {
                return {i, indices[diff]};
            }
        }
        return {};
    }
};