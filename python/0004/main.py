from typing import List


class Solution:
    def findMedianSortedArrays(
            self,
            nums1: List[int],
            nums2: List[int],
    ) -> float:
        A = nums1
        B = nums2
        # Make sure A is the smallest
        if len(nums2) < len(nums1):
            A, B = B, A

        total_size = len(nums1) + len(nums2)
        mid = total_size//2

        left = 0
        right = len(A) - 1

        while True:
            a = (left + right) // 2
            b = mid - a - 2
            a_left = A[a] if a >= 0 else float("-inf")
            a_right = A[a + 1] if a + 1 < len(A) else float("inf")
            b_left = B[b] if b >= 0 else float("-inf")
            b_right = B[b + 1] if b + 1 < len(B) else float("inf")
            if a_left <= b_right and b_left <= a_right:
                if total_size % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right))/2
            elif a_left > b_right:
                right = a - 1
            elif b_left > a_right:
                left = a + 1
