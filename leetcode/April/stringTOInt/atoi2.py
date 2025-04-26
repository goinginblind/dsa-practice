def myAtoi(s: str) -> int:
    return_string = ''  # We will make a string first, then convert it to int
    s = s.strip()  # Strip of leading and trailing spaces
    sign_exists, sign = False, 1  # Assume there's no sign as of yet, so the sign is '+'

    for char in s:
        # Handle chracters that are: alphabetical, signs after 
        # they've already appeared or whitespaces
        if char.isalpha() or (char in ['-', '+'] and sign_exists) or char == ' ' or char == '.':
            break

        if char == '-' and not sign_exists:
            sign = -1
            sign_exists = True
            continue
        elif char == '+' and not sign_exists:
            sign = 1
            sign_exists = True
            continue
        
        if char.isdigit() and char != '0':
            sign_exists = True
            return_string += char
        elif char == '0' and return_string == '':
            sign_exists = True
            continue
        elif char == '0' and return_string != '':
            return_string += char
            sign_exists = True
            continue

    if return_string != '':
        ret_int = int(return_string) * sign
        if ret_int > 2147483647:
            return 2147483647
        elif ret_int < -2147483648:
            return -2147483648
        else:
            return ret_int
        
    else:
        return 0
        



def main():
    atoi_sample = "21474836460"
    atoi_sample2 = '1337c0d3'
    atoi_sample3 = '0-1'
    atoi_sample4 = 'words and 987'
    print(myAtoi(atoi_sample))
    print(myAtoi(atoi_sample2))
    print(myAtoi(atoi_sample3))
    print(myAtoi(atoi_sample4))


main()