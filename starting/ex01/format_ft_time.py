import time
import datetime

# A find method
def ft_find(str, c):
    for i, char in enumerate(str):
        if char == c:
            return i
    return -1

def ft_science(tstr, length):
    if length <= 1:
        return tstr, length
    # scientific notation: first digit, dot, next two digits, e+0, length-1
    sci_str = tstr[0] + '.' + tstr[1:3] + 'e+0' + str(length - 1)
    return sci_str, len(sci_str)

def ft_easy(tstr):
    length = ft_find(tstr, '.')
    if length == -1:
        length = len(tstr)
        
    for c in range(length - 1 - 3, 0, -3):
        tstr = tstr[:c] + '.' + tstr[c:]
    # length is the number of digits before the first dot
    # return type tuple (string, length)
    return tstr, length






if __name__ == "__main__":
    t = time.time()
    tstr = str(round(t, 4))
    
    str1, len1 = ft_easy(tstr)
    # or easier with f-string formatting
    # f"{t:,.4f}": format number with commas and 4 decimals
    # str1 = f"{t:,.4f}".replace(',', '.')
    
    str2, len2 = ft_science(tstr, len1)
    # or easier with f-string formatting
    # f"{t:.4e}": format number in scientific notation with 4 decimals
    # str2 = f"{t:.2e}".replace(',', '.')
    
    print(f"Seconds since January 1, 1970: {str1} or {str2} in scientific notation")
    x = datetime.datetime.now()
    print(f"{x.strftime('%b')} {x.strftime('%d')} {x.strftime('%Y')}")