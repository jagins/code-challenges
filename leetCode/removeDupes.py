def removeDuplicates(self, nums: List[int]) -> int:
    #check to see if the length of the array is 0 and return 0 if it is
    if len(nums) == 0:
        return 0
        
    #i = index of the array and loop through to the end of nums from the 1st element
    i = 0
    for j in range(1, len(nums)):
        #check if they're diffent then increment the index + 1
        if nums[i] != nums[j]:
            i += 1
            #else merge one with the other
            nums[i] = nums[j]
    #return the length of the array + 1
    return i + 1