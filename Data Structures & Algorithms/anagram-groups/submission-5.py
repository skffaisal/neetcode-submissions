class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for ele in strs:
            # print(tuple(sorted(ele)))

            key = tuple(sorted(ele))

            if key not in result:
                result[key]=[ele]
            else:
                # result[key] will be come the value there
                result[key].append(ele)
        # print(result.values())
        return list(result.values())
        
        




    def get_freq(self,n:str):
        freq={}

        for i in range(len(n)):
            freq[n[i]]=freq.get(n[i],0)+1
        
        return freq