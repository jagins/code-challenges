def lengthOfLongestSubstring(s: str) -> int:
    used = {} #stores chars being used
    longest = 0 #length of the longest substring
    start_index = 0 #starting index of the current substring
        
    for i, char in enumerate(s):
        if char in used:
            start_index = max(start_index, used[char] + 1)
            used[char] = i
            longest = max(longest, i - start_index + 1)
    return longest
        