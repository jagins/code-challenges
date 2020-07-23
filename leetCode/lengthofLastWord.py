def lengthofLastWord(s: str) -> int:
    array = s.split()
    
    if len(array) > 0:
        last_index = len(array) - 1
        return len(array[last_index])
    return 0