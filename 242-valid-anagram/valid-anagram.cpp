class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;
        for (char a: s) {
            sMap[a]++;
        }
        for (char b: t) {
            tMap[b]++;
        }
        return (sMap == tMap);
    }
};