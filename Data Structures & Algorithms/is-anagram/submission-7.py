class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting method
        # least effective O(n log n) due to sorting
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)      
        """

        # map/get somewhat efficient
        # map not neededed, doable in 1 for with range 
        """
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for char in s:
            s_map[char] = s_map.get(char,0)+1
        for char in t:
            t_map[char] = t_map.get(char,0)+1    
        return s_map == t_map
        """
        # using freq hash
        if len(s) != len(t):
            return False

        freq_key = [0] * 26
        for char in s:
            freq_key[ord(char) - ord('a')] += 1
        for char in t:
            freq_key[ord(char) - ord('a')] -= 1
        
        return len(set(freq_key)) == 1   
        
       