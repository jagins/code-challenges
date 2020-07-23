def sortColors(nums: List[int]) -> None:
    length = len(nums)
    
    for i in range(length):
        for j in range(length - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] =  temp
    return nums