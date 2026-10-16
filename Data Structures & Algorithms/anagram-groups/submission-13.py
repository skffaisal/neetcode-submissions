class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        
        
        d={}

        for i in range(len(s)):
            key=[0]*26
            for char in s[i]: # each individual string
                # print(char)
                # print(ord(char)-ord('a'))
                key[ord(char)-ord('a')]+=1
                
            if tuple(key) not in d:
                d[tuple(key)]=[s[i]]
            else:
                d[tuple(key)].append(s[i])

            
        # print(d.values())
        return list(d.values())
                
            

        
        



