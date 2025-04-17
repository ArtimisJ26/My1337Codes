class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size()-1;

        while(left < right){
            int curr = numbers[left] + numbers[right];
            if(curr == target){
                return{left + 1, right + 1};
            } else if (curr > target) {
                right--;
            } else {
                left++;
            }
        }
        return {};
    }
};