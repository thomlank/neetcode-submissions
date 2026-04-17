class Solution:
    def encode(self, strs: List[str]) -> str:
        # coded = ""
        # for word in strs:
        #     coded +=f"{len(word)}#{word}"      
        # return coded

        # refactored
        return "".join([f"{len(word)}#{word}" for word in strs])

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded        
        
            