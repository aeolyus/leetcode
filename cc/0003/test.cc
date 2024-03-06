#include "sol.h"
#include <gtest/gtest.h>
#include <vector>

struct TestCase {
  string s;
  int expected;
  TestCase(string s, int i) : s(s), expected(i) {}
};

TEST(Test0003, BasicTestCases) {
  Solution sol;
  vector<TestCase> testCases = {
      {"abcabcbb", 3},
      {"bbbbb", 1},
      {"pwwkew", 3},
  };
  for (const auto &tc : testCases) {
    EXPECT_EQ(tc.expected, sol.lengthOfLongestSubstring(tc.s));
  };
}
