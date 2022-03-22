def containsDuplicate(nums):
        nums.sort()
        print(len(nums))
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                return True
        return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([2,14,18,22,22]))


