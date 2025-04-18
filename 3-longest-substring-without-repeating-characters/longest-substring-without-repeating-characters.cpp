class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen;
        int l = 0, r = 0, res = 0;

        while (r < s.size()) {
            // cout << l << ", " << r;
            char curr = s[r];

            if (seen.count(curr)) {
                if (seen[curr] >= l) {
                    l = seen[curr] + 1;
                }
            }
            seen[curr] = r;

            res = max(res, r - l + 1);
            r++;
        }
        return res;
    }
};