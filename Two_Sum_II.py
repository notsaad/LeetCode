class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L, R = 0, len(numbers) - 1

        while L > -1 and R < len(numbers):
            total = numbers[L] + numbers[R]
            if total == target:
                return [L + 1, R + 1]
            elif total < target:
                L += 1
            else:
                R -= 1
