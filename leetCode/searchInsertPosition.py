def searchInsert(self, nums: List[int], target: int) -> int:
    length = len(nums)
    for i in range(length):
        if nums[i] >= target:
            return i
    return i + 1