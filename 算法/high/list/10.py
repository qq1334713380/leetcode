class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k==0:
            return []
        nums.append(-65536)
        list_num = []
        for i in range(k,len(nums)):
            list_num.append(max(nums[i-k:i]))
        return list_num
    
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))