class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num,0) + 1   
        # return list(num_count.keys())[-k:]
        sorted_count = (sorted(num_count.items(), key = lambda kv: (kv[1],kv[0])))
        return [pair[0] for pair in sorted_count[-k:]]  
            