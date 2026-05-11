class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to check if target in sorted side vs pivot side
        # check middle value to target
        # if loop ends target not found 
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
