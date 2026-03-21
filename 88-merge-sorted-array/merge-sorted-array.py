class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l3=[]
        j=0
        k=0
        while(j<m and k<n):
            if(m!=0 and nums1[j]<nums2[k]):
                l3.append(nums1[j])
                j+=1
            elif(n!=0 and nums2[k]<=nums1[j]):
                l3.append(nums2[k])
                k+=1
        while(k==n and j<m):
            l3.append(nums1[j])
            j+=1
        while(j==m and k<n):
            l3.append(nums2[k])
            k+=1
        for i in range(len(l3)):
            nums1[i]=l3[i]