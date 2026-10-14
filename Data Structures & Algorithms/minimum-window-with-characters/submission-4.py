class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        min_len=float('inf')
        res_str=''

        freq_t={}
        for i in range(len(t)):
            freq_t[t[i]]=freq_t.get(t[i],0)+1

        # how many chareacters required to make the window valid
        required = len(freq_t)

        # How many same mapped charaters from string t found in the window
        found =0 # this variable counts satisfied character types, not the total number of characters.

        # ie if string t has 2 "A" s , found will be incremented by one when 2 "A" s are found in the window

        # ultimately the window will be valid if found == required

        l=0
        window={}
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            # is this char (s[r]) in the string t ?
            # and 
            # is s[r] window count equal to that of the string t 
            if s[r] in freq_t and window[s[r]] == freq_t[s[r]]: # it needs to match exactly, becasue the string t could have duplicates as well
                found+=1
            
            while found == required: # found a valid window
                if min_len > (r-l+1): # save the substring 
                    min_len=r-l+1
                    res_str = s[l:r+1]

                # check if the left character, the one we about to remove, is the character in the string t , by which we had incremented the   found variable
                # and the frequency of that character in the window is exactly equal to that of the the string t, then it will mean by removing that char, one of the conditions will not meet and found will be decremented
                if s[l] in freq_t and window[s[l]]==freq_t[s[l]]:
                    found-=1

                # shrink the window from left 
                window[s[l]]=window.get(s[l],0)-1
                l=l+1

        return res_str




            

            
            

        




