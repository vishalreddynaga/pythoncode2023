#Leetcode_Remove_Elements

l =[]

class Solution:
    def removeElements(self , nums , target):
        i = 0 
        for n in nums:
            if n != target:
                i = i+1
        return i
            

s = Solution()
s.removeElements([0,1,2,2,3,0,4,2], 2)
