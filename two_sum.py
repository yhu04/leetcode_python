
#Brute Force n^2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
        return [-1,-1]

# n 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary for the list and its indice
        nums_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in nums_dict:
                return [nums_dict[target-nums[i]],i]
            nums_dict[nums[i]]=i
        # no result
        return [-1,-1]
  
