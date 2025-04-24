class Solution {
public:
    int rob(vector<int>& nums) {
        int rob1 = 0, rob2 = 0, temp;

        for (int n : nums) {
            temp = max(n + rob1, rob2);
            cout << rob1 << " " << rob2 << endl;
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }
};