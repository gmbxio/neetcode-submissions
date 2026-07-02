class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)

        totalLen = m + n
        halfLen = (totalLen + 1) // 2

        left, right = 0, m

        while left <= right:
            i = left + (right - left) // 2
            j = halfLen - i

            leftnum1 = nums1[i - 1] if i > 0 else float("-inf")
            leftnum2 = nums2[j - 1] if j > 0 else float("-inf")

            rightnum1 = nums1[i] if i < m else float("inf")
            rightnum2 = nums2[j] if j < n else float("inf")

            if leftnum1 <= rightnum2 and leftnum2 <= rightnum1:
                if totalLen % 2 != 0:
                    return (float(max(leftnum1, leftnum2)))
                else:
                    return float((max(leftnum1, leftnum2) + min(rightnum1, rightnum2)) / 2)
            

            elif leftnum1 > rightnum2:
                right = i - 1
            else:
                left = i + 1
