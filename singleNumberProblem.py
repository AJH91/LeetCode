from collections import Counter

def singleNumber(nums):
    c = Counter(nums)
    for x in c.values():
          if x==1:
              return (list(c.keys())[list(c.values()).index(1)])


print(singleNumber([4,1,2,1,2]))
print(singleNumber([2,2,1]))
print(singleNumber([1]))


