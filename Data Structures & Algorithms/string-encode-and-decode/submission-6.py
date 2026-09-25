class Solution:

    def encode(self, strs: List[str]) -> str:
        result=''

        for i in range(len(strs)):
            result+=str(len(strs[i]))+'|'+strs[i]
        return result
        

    def decode(self, s: str) -> List[str]:

        print(s)

        result=[]

        

        i=0 # pointer im using to point to start of the string
        j=i # pointer for end of the string. ie initially both are at index 0
        while i<len(s):

            # find the first delimeter 
            while s[j] != '|':
                j+=1

            # now j is at the the delimeter 
            length=int(s[i:j])

            i=j+1 # placing at start of the first string 
            j=j+1 # placing j also there 

            j= i+length # calculating the end (no in list this will be exclusive)

            result.append(s[i:j]) # placing the first string in the list

            i=j # moving both pointers to identify the next string

            # 5|hello5|world
        return result








