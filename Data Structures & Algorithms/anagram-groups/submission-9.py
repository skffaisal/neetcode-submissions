class Solution:
    def groupAnagrams(self, n: list[str]) -> list[list[str]]: # N words × K characters= O(NK)
        # assume the input strings will be in lower case only, 
        dict={}

        for i in range(len(n)):
            key = self. get_freq_list(n[i])

            if key not in dict:
                dict[key]=[n[i]]
            else:
                dict[key].append(n[i])
        return list(dict.values())

    def get_freq_list(self,s:str):
        list=[0]*26
        for i in range (len(s)):
            index= ord(s[i])-ord('a')
            list[index]+=1
        return tuple(list)
        




    def get_freq(self,n:str):
        freq={}

        for i in range(len(n)):
            freq[n[i]]=freq.get(n[i],0)+1
        
        return freq