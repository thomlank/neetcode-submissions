class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Brute 
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
        if len(s) != len(t):
            return False
        freq_key = [0] * 26
        for char in s:
            freq_key[ord(char) - ord('a')] += 1
        for char in t:
            freq_key[ord(char) - ord('a')] -= 1
        
        return len(set(freq_key)) == 1    