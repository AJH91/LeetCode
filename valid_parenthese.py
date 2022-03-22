from collections import deque

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    d = deque()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            d.append(ch)
        if ch==')' or ch=='}' or ch == ']':
            if d.__len__()==0:
                return False
            matching_pairs = {')': '(',']': '[','}': '{'}
            if matching_pairs[ch] != d.pop():
                return False
    return d.__len__()==0



print(is_balanced("()"))
print(is_balanced("(),[],{}"))
print(is_balanced("(]"))