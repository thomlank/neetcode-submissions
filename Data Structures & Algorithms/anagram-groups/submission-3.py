class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_bank = {}
        for word in strs:
            char_freq = [0] * 26
            for char in word:
                # convert to ascii value to get index
                char_freq[ord(char) - ord("a")] += 1
            # creates dict entry or adds to it 
            word_bank.setdefault(tuple(char_freq), []).append(word)
        return list(word_bank.values())