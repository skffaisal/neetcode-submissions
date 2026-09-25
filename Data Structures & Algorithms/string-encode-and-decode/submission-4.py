class Solution:

    def encode(self, strs: List[str]) -> str:

        # length + delimenter + string

        result=""

        for i in range (len(strs)):
            result+=str(len(strs[i]))+'|'+strs[i]

        return result 


    def decode(self, s: str) -> List[str]:

        print(s)

        result=[]
        length_str=''
        length_num=0

        # check delimenter

        # if delemeter found, covert elemets before the delimeter to interger, that will be the count 

        #next count elemts will the the string 

        i=0 
        j=0
        while i< len(s):
            print(s[i])

            if (s[i]=="|"):
                length_str=s[j:i] # j is start, i-1 is the end
                length_num=int(length_str)

                print(f"extracted integer: {length_num}")

                j=(i+1)+length_num  # i+1 is the start of the actual string 

                result.append(s[i+1:j])
                
                i=j
                
            i=i+1
        print(result)
        return result



            








