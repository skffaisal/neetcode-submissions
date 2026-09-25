class Solution:
    def productExceptSelf(self, n: List[int]) -> List[int]:
        # asuming divisionis allowed, 
        zeros_count=0
        product=1
        one_zero_index=0
        result=[0]* len(n)

        for i in range(len(n)):
            if n[i]!=0:
                product*=n[i]
            else:
                zeros_count+=1
                one_zero_index=i

        # if exactly one zero in list, all other positions other than that position will be zero in the result
        if zeros_count == 1:
            result[one_zero_index]=product
            return result
            
         # if more than one zeros, whole list will be zero in the result
        if zeros_count>1:
            return result

        #no zeros 
        for i in range(len(n)):
            result[i]=product//n[i]
        
        return result


        