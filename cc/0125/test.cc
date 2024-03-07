#include "sol.h"
#include <gtest/gtest.h>
#include <vector>

struct TestCase {
  string s;
  bool expected;
  TestCase(string s, bool b) : s(s), expected(b) {}
};

TEST(Test0125, BasicTestCases) {
  Solution sol;
  vector<TestCase> testCases = {
      {"A man, a plan, a canal: Panama", true},
      {"race a car", false},
      {" ", true},
  };
  for (const auto &tc : testCases) {
    EXPECT_EQ(tc.expected, sol.isPalindrome(tc.s));
  };
}
