class Solution {
public:
    string decodeString(string s) {
        vector<string> st;
        int i = 0;

        for (int  i = 0; i < s.size(); i++){
            if (s[i] != ']') st.push_back(string(1, s[i]));
            else{
                string subStr;
                while (st.back() != "["){
                    subStr = st.back() + subStr;
                    st.pop_back();
                }
                st.pop_back();  // pop out the opening bracket
                string f = "";
                while (!st.empty() && isdigit(st.back()[0])) {
                    f = st.back() + f;
                    st.pop_back();
                }
                int repeatCount = stoi(f);

                string repeatedStr = "";
                for (int j = 0; j < repeatCount; j++) {
                    repeatedStr += subStr;
                }
                st.push_back(repeatedStr);
            }
        }

        string res = "";
        for (string c : st){
            res += c;
        }
        return res;
    }
};