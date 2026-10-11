class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=''

        for i in range(len(strs)):
            encoded_string+= str(len(strs[i]))+'|'+strs[i]

        return encoded_string


    def decode(self, s: str) -> List[str]:
        res=[]
        a2=0
        a1=0 
        
        while a2<len(s):
            while s[a2]!='|':
                a2=a2+1
            
            lent=int(s[a1:a2])
            print(lent)
            a2=a2+1 # moved from the delimeter
            res.append(s[a2:a2+lent])           
            
            a2=a2+lent # skip the appended ones
            a1=a2 # for the next word
        return (res)

            
            
