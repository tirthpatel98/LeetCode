# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums1 = nums[:]
        i = len(nums)-2
        flag=0
        while i >= 0:
            curr = nums[i]
            maxi = 101
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i] and nums[j] < maxi:
                    maxi=nums[j]
                    ind=j
            if maxi!=101:
                nums[i],nums[ind] = nums[ind],nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                flag=1   
            if flag == 0:
                i-=1
            else:break
    
        if nums == nums1:
            nums[0:]=sorted(nums)
            
        
