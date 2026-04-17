class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False       
        punc_stack = []
        punc_close = {
            ")":"(",
            "]":"[",
            "}":"{"
        } 
        for char in s:
            if char in punc_close.values():
                punc_stack.append(char)
            elif punc_stack and punc_close[char] == punc_stack[-1]:
                punc_stack.pop()
            else:
                return False
        return len(punc_stack) == 0              