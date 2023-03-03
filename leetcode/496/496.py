class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        r = []
        for i in nums1:
            ind = nums2.index(i)
            for j in nums2[ind:]:
                if j > i:
                    r.append(j)
                    break
            else:
                r.append(-1)
        
        return r
                
