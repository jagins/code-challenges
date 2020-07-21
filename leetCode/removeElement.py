def removeElement(self, nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return 0
        
    index = 0
    while index < len(nums):
        if nums[index] == val:
            nums.pop(index)
        else:
            index += 1
        
    return len(nums)