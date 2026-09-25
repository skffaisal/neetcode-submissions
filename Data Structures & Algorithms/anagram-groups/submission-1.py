class Solution:
    def groupAnagrams(self, n: list[str]) -> list[list[str]]:
        # hint: sort each word to get canonical key , then add in dict 
        dict={}
        
        for i in range(len(n)):
            key = self.get_freq_list(n[i])
            
            

            # here im thinking somehow convert this key variable from dict type to something , so that i can make it a a key in a dictionary
            if key not in dict:
                dict[key]=[n[i]]
            else:
                dict[key].append(n[i])
       
        return list(dict.values())


    def get_freq_list(self,s:str):
        freq=[0]*26
        for i in range(len(s)):
            index=ord(s[i])-ord('a')
            freq[index]+=1
        return tuple(freq)
            

