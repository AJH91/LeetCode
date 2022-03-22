def isPalindrome(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    reverseString = s[::-1]
    return s == reverseString

print(isPalindrome("A man, a plan, a canal: Panama"))




