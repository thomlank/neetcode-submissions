class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute
        """
        result = []
        for i in range(len(nums)):
            prod = 1
            for iNum,num in enumerate(nums):
                if iNum != i:
                    prod *= num
            result.append(prod)
        return result
        """ 

        # Guided
        result = [1] * (len(nums)) # init array for in place math

        prefix = 1
        for i in range(len(nums)):
            # iter through nums l to r
            result[i] = prefix
            # stores result from last iter
            # ie: this makes it so 3rd element in result holds the product of elements 0-2
            prefix *= nums[i]
            # calc prod of default or up to current element, to be stored for next pass 

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            # iter through nums r to l
            result[i] *= postfix
            # like above but since result already holds value, we multiply with whats stored
            postfix *= nums[i]
             
        return result              