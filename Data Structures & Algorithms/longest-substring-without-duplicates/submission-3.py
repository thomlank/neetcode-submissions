class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # early out
        if s == None or s == "":
            return 0
        
        max_sub = 0
        l = 0
        is_dup = set()
        # increase r pointer constant, shrinks window with l on duplicate
        for r in range(len(s)):
            while s[r] in is_dup:
                is_dup.remove(s[l])
                l += 1
            is_dup.add(s[r])
            # checks set length to get largest
            # max_sub = len(is_dup) if len(is_dup) > max_sub else max_sub
            # better max check:
            window = (r-l) + 1
            max_sub = max(max_sub, window)
        return max_sub