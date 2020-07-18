def reverse(self, x: int) -> int:
    reverse_string = [i for i in str(x)]
        
    if reverse_string[0] == '-':
        reverse_string.pop(0)
        
        reverse_string.reverse()
     
    #check for overflow of a 32 bit number
    if int(''.join(reverse_string)) > (2 ** 31 - 1):
        return 0
    #check if it's less than 0 to re-add the sign
    if x < 0:
        return -int(''.join(reverse_string))
    else:
        return int(''.join(reverse_string))
        