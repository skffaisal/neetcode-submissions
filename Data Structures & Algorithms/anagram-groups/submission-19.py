class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res={}

        for s in strs:

            key=[0]*26

            for char in s:
                key[ord(char)-ord('a')]+=1

            if tuple(key) not in res:
                res[tuple(key)]=[s]
            else:
                res[tuple(key)].append(s)

        return(list(res.values()))