class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)
        l = 1
        while numbers[l-1] + numbers[r-1] != target:
            if numbers[l-1] + numbers[r-1] < target:
                l += 1
            else:
                r -= 1    
        return [l,r]    

        