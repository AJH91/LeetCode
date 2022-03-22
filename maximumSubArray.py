def maxSubArray(nums):
    maxSoFar = -9999999999999999
    runningCount = 0

    for x in range(0,len(nums)):
        runningCount += nums[x]
        if (maxSoFar < runningCount):
            maxSoFar = runningCount
        if (runningCount < 0):
            runningCount = 0
    return maxSoFar

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))






