class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        if len(nums1)==1:
            return nums1[0]
        nums1.sort()
        if len(nums1) % 2 != 0:
            return (float(nums1[int(len(nums1) / 2)]))
        else:
            return (float(nums1[int(len(nums1) / 2)-1] + float(nums1[int(len(nums1) / 2)])) / 2)
