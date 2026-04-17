class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        orig_len = len(nums)
        if orig_len == 3 and sum(nums) == 0:
            return [nums]
        nums.sort()
        result = []

        for i in range(orig_len - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = orig_len - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] == target: 
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1          
                elif nums[l] + nums[r] < target:
                    l += 1
        return result