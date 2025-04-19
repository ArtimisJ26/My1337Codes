class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        unordered_map<char, char> pairs = {
            {'}','{'}, 
            {')','('}, 
            {']','['}
        };

        for (char c : s) {
            if (c == '{' || c == '(' || c == '[') {
                stk.push(c);
            } else {
                if (stk.empty()) return false;
                if (pairs[c] != stk.top())  return false;
                stk.pop();
            }
        }
        if (stk.empty()) return true;
        return false;
    }
};