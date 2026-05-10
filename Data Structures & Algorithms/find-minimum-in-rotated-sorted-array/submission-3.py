class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n)
        # min_value = nums[0]
        # for i in range(0,len(nums),2):
        #     if min_value < nums[i]:
        #         continue
        #     min_value = min(min_value, nums[i], nums[i-1])
        # return min_value
        
        # wip
        find_mid = lambda rgt,lft: (rgt - lft) // 2
        l = 0
        r = len(nums) - 1
        mid = find_mid(r,l)
        print(f'starting l:{nums[l]} m:{nums[mid]} r:{nums[r]}')

        # early out
        if nums[l] < nums[mid] < nums[r] or len(nums) == 1:
            return nums[l]
        
        while l+1 != r:
            # move right
            if nums[l] < nums[mid] : 
                l = mid
                mid += find_mid(r,l)
            # move left
            else: 
                r = mid
                mid -= find_mid(r,l)
        return min(nums[l],nums[r])                