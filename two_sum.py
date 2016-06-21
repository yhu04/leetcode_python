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
  
