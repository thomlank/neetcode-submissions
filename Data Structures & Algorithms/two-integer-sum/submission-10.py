class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i,num in enumerate(nums):
            print(f'i:{i} num:{num}')
            if num not in comp_map:
                comp_num = (target - num) 
                comp_map[comp_num] = i
                print(comp_map)
            else:
                return [comp_map[num],i]        