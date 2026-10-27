class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            key=[0]* 26
            for char in word:
                key[ord(char)-ord('a')]+=1
            key=tuple(key)

            if key not in d:
                d[key]=[word]
            else:
                d[key].append(word)
        return list(d.values())