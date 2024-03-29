class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length=len(digits)
        if length==0:
            return digits
        carry=1
        for i in range(length-1,-1,-1):
            
            digits[i],carry=(digits[i]+carry)%10,(digits[i]+carry)//10
            if carry==0:
                break
        if carry==1:
            return [1]+digits
        else:
            return digits
        
    '''    
    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits
    '''
