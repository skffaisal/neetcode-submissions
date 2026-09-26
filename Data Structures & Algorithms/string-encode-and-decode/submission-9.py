class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for ele in strs:
            result += str(len(ele)) + '|' + ele
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 
        j = 0
        while j < len(s):
            if s[j] == "|": 
                word_length = int(s[i:j]) 
                j = j + 1 # move past the delimiter
                
                result.append(s[j:j+word_length])

                j = j + word_length # move to the start of the next length prefix
                i = j
                # Do NOT increment j here; we are already at the next valid starting position
            else:
                j = j + 1 # only increment when looking for the delimiter
                
        return result