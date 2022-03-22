def lengthOfLastWord(s: str):
    counter = 0
    size = len(s) - 1
    if size<=1:
        return 1
    for x in range(size, 0, -1):
        if s[x] == ' ':
            continue
        else:
            while s[x] != ' ' and x>=0:
                counter += 1
                x-= 1
            else:
                break
    return counter



print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("World"))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("a"))
print(lengthOfLastWord("a "))
print(lengthOfLastWord("day"))

