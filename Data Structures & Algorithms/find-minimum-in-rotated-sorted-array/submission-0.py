class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        for i in range(0,len(nums),2):
            if min_value < nums[i]:
                continue
            min_value = min(min_value, nums[i], nums[i-1])
        return min_value