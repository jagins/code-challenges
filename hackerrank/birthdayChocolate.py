def birthday(s, d, m):
    if len(s) == 0:
        return 0
    
    if len(s) == 1:
        return 1
    
    array = []
    
    for i in range(len(s) - 1):
        array.append(s[i: i + m])
        
    sum = 0
    count = 0
    
    for tup in array:
        for j in tup:
            sum += j
        if sum == d:
            count += 1
            
        sum = 0
    
    return count