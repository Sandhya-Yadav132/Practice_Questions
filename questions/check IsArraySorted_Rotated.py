#Ques : You are given an array of integers. You need to determine whether the array is sorted in non-decreasing order (ascending order with duplicates allowed).
#If the array is sorted, return true, otherwise return false.

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        n=len(nums)
        for i in range(n):
           if nums[i]>nums[(i+1)%n]:  #*
               count+=1
        return count<=1  #**

  #NOTE: Agar interviewer puche:
'''
** "Sorted rotated array me max 1 hi break hota hai"
* 👉 “Why % n?”
“Circular array treat karne ke liye, last element ko first se compare karne ke liye.'''
