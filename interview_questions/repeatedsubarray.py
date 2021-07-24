# Given two integer arrays nums1 and nums2, 
# return the maximum length of a subarray that appears in both arrays.
# Example 1:
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:

# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

from typing import List
from typing import Dict
from collections.abc import Sequence
from typing import Union

class Solution:
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        print (memo)
        import pdb
        for i in range(len(A) - 1, -1, -1):
            pdb.set_trace()
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        # return max(max(row) for row in memo)

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,4,5]
    nums2 = [2,1,3,4]
    s.findLength(nums1, nums2)