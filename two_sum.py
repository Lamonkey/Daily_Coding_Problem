from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        #store number in hash table
        for i in range(len(nums)):
            num = nums[i]
            #check if number target - i exist in dictionary
            diff = target - num
            if((numbers.get(diff,None) is not None) ):
                return [i,numbers.get(diff)]
            #key is num, value is index
            numbers[num] = i
sol = Solution()

print(sol.twoSum(nums = [2,7,11,15],target = 9))
print(sol.twoSum(nums = [3,3],target = 6))
       
        
            
            
        