class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = {} # (freq tuple) : [grouping]    
        for word in strs:
            freq_key = [0] * 26
            for char in word:
                freq_key[ord(char)-ord('a')] += 1
            freq_key = tuple(freq_key)    
            if freq_key not in group_map:
                group_map[freq_key] = [word]
            else:
                group_map[freq_key] += [word]       
        return list(group_map.values())          
        

        