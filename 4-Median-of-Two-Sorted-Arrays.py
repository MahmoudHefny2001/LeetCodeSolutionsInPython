class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = nums1 + nums2

        merged = sorted(merged)

        if len(merged) % 2 != 0:
            return merged[len(merged) // 2]
        
        return ((merged[(len(merged) // 2) - 1] + merged[(len(merged) // 2)] )) / 2 