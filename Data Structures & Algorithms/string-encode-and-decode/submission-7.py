class Solution:

    def encode(self, strs: List[str]) -> str:
        # length+delimeter +string
        result=""
        for ele in strs:
            result+=str(len(ele))+'|'+ele
        return result

    def decode(self, s: str) -> List[str]:
        # print(s)
        # read until you find the delimeter
        result=[]
        i=0 # 
        j=0
        while j<len(s):
            if s[j]=="|": # delimeter found
                word_length=int(s[i:j]) # excluding the last index
                # print(word_length)
                j=j+1 # pointing j next to the delimeter 
                
                result.append(s[j:j+word_length])

                j=j+word_length
                i=j
            j=j+1
        return (result)

                    






