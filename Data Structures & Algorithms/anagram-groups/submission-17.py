class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)

        for s in strs:

            key=[0]*26

            for char in s:
                key[ord(char)-ord('a')]+=1

            res[tuple(key)].append(s)
            
        return(list(res.values()))