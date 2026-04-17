import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = s.lower()
        filtered = re.findall(r'[a-z0-9]',lower_case)
        left,right = 0, len(filtered) -1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1    
        return True        
        