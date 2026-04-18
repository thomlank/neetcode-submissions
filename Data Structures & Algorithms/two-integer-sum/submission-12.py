class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge early term space complex reduction
        if len(nums) == 2 and sum(nums) == target:
            return [0,1]

        sum_map = {}
        for dex, num in enumerate(nums):
            if num in sum_map:
                return [sum_map[num], dex]
            # stores complimentary to num to make target as key, index as val
            sum_map[target - num] = dex    
                   