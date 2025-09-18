class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t=[]
        i,j=0,0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                t.append(nums1[i])
                i+=1
            else:
                t.append(nums2[j])
                j+=1
        while i<m:
            t.append(nums1[i])
            i+=1
        while j<n:
            t.append(nums2[j])
            j+=1
        for k in range(m+n):
            nums1[k]=t[k]
        