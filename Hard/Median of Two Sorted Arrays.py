class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        l=m+n
        
        if m==0:
            if n%2 ==0:
                return (nums2[(n//2)-1]+nums2[n//2])/2
            else:
                return nums2[n//2]
        if n==0:
            if m%2 ==0:
                return (nums1[(m//2)-1]+nums1[m//2])/2
            else:
                return nums1[m//2]
        
        return self.findKth(nums1,nums2,l//2) if l%2==1 else (self.findKth(nums1,nums2,l//2-1)+self.findKth(nums1,nums2,l//2))/2.0
    
    def findKth(self,A,B,k):
        
        i,j=0,0
        while k > 0:
            if i== len(A):
                return B[j+k]
            if j==len(B):
                return A[i+k]
            
            if A[i] <= B[j]:
                i+=1
            else:
                j+=1
            k-=1
        
        if i >= len(A):
            return B[j]
        if j >= len(B):
            return A[i]
        return min(A[i],B[j]) #2
