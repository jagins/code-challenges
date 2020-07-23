def majorityElement(nums: List[int]) -> int:
    table = {}
    size = len(nums)
    
    for i in nums:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    
    for key in table:
        if table[key] > size / 2:
            return key