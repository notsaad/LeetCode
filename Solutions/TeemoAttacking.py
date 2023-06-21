class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        res = 0
        count = 0

        for i, v in enumerate(timeSeries):
            if i == 0:
                count = v + duration - 1
                res += duration
            else:
                if v > count:
                    res += duration
                    count = v + duration - 1
                else:
                    if (v + duration - 1) - count > 0:
                        res += (v + duration - 1) - count
                    count = v + duration - 1

        return res
