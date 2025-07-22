"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # pointers to the last valid elements in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # pointer to the very end of nums1
        last = m + n - 1

        # While there are still elements in nums2, pick the larger tail from nums1 or nums2
        while p2 >= 0:
            # If nums1 is exhausted (p1 < 0), or nums2[p2] is bigger, take from nums2
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else:
                nums1[last] = nums1[p1]
                p1 -= 1
            last -= 1

















        if n < 1:
            return

        if m == 0 and n > 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return

        # reverse pass on nums1
        # we will compare the largest values from the endings of the 2 lists
        # and construct the sorted list from max val to min val
        # only this way allows us to mess up nums1 since its full on the first part [x,y,z, ... 0,0,0]
        m -= 1
        n -= 1
        for i in range(len(nums1) -1, -1, -1):

            if n == -1:  # if the nums2 list is exhausted
                break

            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:  # nums1[m] < nums2[n]
                nums1[i] = nums2[n]
                n -= 1


if __name__ == '__main__':
    sol = Solution()

    examples = [
        # Example 1
        {
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [2, 5, 6],
            "n": 3,
        },
        # Example 2
        {
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
        },
        # Example 3
        {
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
        },
        # Additional Example 4
        {
            "nums1": [4, 5, 6, 0, 0, 0],
            "m": 3,
            "nums2": [1, 2, 3],
            "n": 3,
        },
        # Additional Example 5
        {
            "nums1": [2, 0],
            "m": 1,
            "nums2": [1],
            "n": 1,
        },
    ]

    for idx, ex in enumerate(examples, start=1):
        nums1 = ex["nums1"].copy()  # copy so we can reprint original
        m = ex["m"]
        nums2 = ex["nums2"].copy()
        n = ex["n"]

        print(f"Example {idx}:")
        print(f"Input nums1 = {nums1}, m = {m}")
        print(f"      nums2 = {nums2}, n = {n}")

        sol.merge(nums1, m, nums2, n)

        print(f"Result nums1 = {nums1}")
        print("------------")