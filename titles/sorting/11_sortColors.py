def sortColors(self, nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j]>nums[j+1]:
                nums[j+1], nums[j]= nums[j], nums[j+1]
    return nums