class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequecy, so going with hash map

        freq1=sorted(s)
        freq2=sorted(t)

        if freq1==freq2:
            return True
        else:
            return False
    
    def get_freq(self, n: str)->dict:

        freq={}
        for i in range (len(n)):
            freq[n[i]]=freq.get(n[i],0)+1
        return freq
        