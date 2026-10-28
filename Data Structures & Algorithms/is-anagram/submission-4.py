class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}
        f2={}
        for i in range(len(s)):
            f1[s[i]]=f1.get(s[i],0)+1
        
        for i in range(len(t)):
            f2[t[i]]=f2.get(t[i],0)+1

        return f1==f2