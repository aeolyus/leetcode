#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    int result = 0;
    int curr = 0;
    unordered_map<char, int> seen;
    for (size_t i = 0; i < s.size(); i++) {
      char ch = s[i];
      if (seen.find(ch) != seen.end() && seen[ch] >= curr) {
        curr = seen[ch] + 1;
      } else {
        result = max(result, int(i) - curr + 1);
      }
      seen[ch] = i;
    }
    return result;
  }
};
