class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        starts = []
        setNums = set(nums)

        for x in range(len(nums)):
            if nums[x] - 1 not in setNums:
                starts.append(nums[x])
        
        i, j = 0, 1
        res, runningCount = 0, 1

        while i < len(starts):
            if starts[i] + j in setNums:
                runningCount += 1
                j += 1
            else:
                j = 1
                i += 1
                if runningCount > res:
                    res = runningCount
                runningCount = 1

        return res
