"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack: list[str] = []
        map_par: dict[str, str] = {'(': ')',
                                   '[': ']',
                                   '{': '}'}

        for char in s:
            if char in {'(', '[', '{'}:
                stack.append(char)

            elif char in {')', ']', '}'}:
                # stack.peek
                peek_val = map_par.get(stack[-1]) if len(stack) > 0 else None

                if char == peek_val:
                    stack.pop()
                else:
                    return False
            else:
                raise ValueError("Invalid character in input")

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("((((()))))", True),
        ("", True),
        (")(", False),
        ("(((", False),
        ("(()))", False),
        ("[({})]", True),
        ("[(])", False),
        ("[", False),
        ("]", False),
    ]

    for idx, (input_str, expected) in enumerate(test_cases, start=1):
        result = s.isValid(input_str)
        print(f"Test {idx:>2}: Input = '{input_str}' → Output = {result} (Expected: {expected})")