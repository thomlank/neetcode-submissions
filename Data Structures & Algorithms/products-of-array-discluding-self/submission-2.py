class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = 1
            for iNum,num in enumerate(nums):
                if iNum != i:
                    prod *= num
            result.append(prod)
        return result        