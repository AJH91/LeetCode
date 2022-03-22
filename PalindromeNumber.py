class Solution:
    def isPalindrome(self, x: int) -> bool:
        intConvertToString = str(x)
        reverseString = intConvertToString[::-1]
        return intConvertToString == reverseString