class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        set<int> numbers;
        int maxim = 0;

        for (int i : nums) {
            maxim = max(maxim, i);
            numbers.insert(i);
        }

        int j = 1;
        while (j < maxim){
            if (numbers.find(j) == numbers.end()) return j;
            j++;
        }
        return maxim + 1;
    }
};