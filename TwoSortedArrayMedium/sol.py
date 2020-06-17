from typing import List
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        start = 0
        end = min(len(nums1),len(nums2))
        xList = nums1 if len(nums1) <= len(nums2) else nums2
        yList = nums2 if len(nums2) > len(nums2) else nums1
        while True:
            partitionX = int((end - start) / 2)
            partitionY = int((len(xList) + len(yList) + 1) / 2) - partitionX
            
            leftX = xList[0 : partitionX]
            rightX = xList[partitionX : ]

            leftY = yList[ 0 : partitionY]
            rightY = yList[ partitionY : ]

            
            for list in [leftX,leftY]:
                if len(list) == 0:
                    list.append(float("-inf"))

            for list in [rightX,rightY]:
                if len(list) == 0:
                    list.append(float("inf"))
 

            if leftX[-1] <= rightY[0] and leftY[-1] <= rightX[0]:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (rightX[-1] + leftY[0])/2
                else:
                    return rightX[-1]
    
            elif leftX[-1] > rightY[0]:
                start =  start + int((end - start) / 2)
            elif leftY[-1] > rightX[0]:
                end = end + int((end-start)/2)

driver = Solution()
nums1 = [1,2,3,4]

nums2 = [5,6]

print(driver.findMedianSortedArrays(nums1,nums2))



                
            
