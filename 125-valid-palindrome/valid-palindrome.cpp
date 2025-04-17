class Solution {
public:
    bool isPalindrome(string s) {
        string t = "";
        for (char c : s) {
            if (isalnum(c)) {
                t += tolower(c);
            }
        }
        
        int l = 0, r = t.size() - 1;

        while (l < r) {
            if (t[l] != t[r]) return false;
            l++;
            r--;
        }
        return true;
    }
};