"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits: list[int] = []
        while x != 0:
            digits.append(x % 10)
            x //= 10

        i, j = 0, len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1122332211))
    print(s.isPalindrome(1233210))
    print(s.isPalindrome(598))
    print(s.isPalindrome(5780875))

