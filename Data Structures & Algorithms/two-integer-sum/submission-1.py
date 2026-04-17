class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_holder = {}
        for idx, num in enumerate(nums):
            pair = target - num
            if pair in num_holder:
                return [num_holder[pair],idx]
            num_holder[num] = idx   
        