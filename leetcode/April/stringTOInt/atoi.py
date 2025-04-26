def myAtoi(s: str) -> int:
    return_string = ''  # We will make a string first, then convert it to int
    s = s.strip()  # Strip of leading and trailing spaces
    sign_exists, sign = False, 1  # Assume there's no sign as of yet, so the sign is '+'

    for char in s:
        # Check for alpha or for whitespace, stop if so
        if char.isalpha() or char == ' ':
            break

        # Check if it's signed, if negative and sign has not been assigned by string, assign sign
        if char == '-' and not sign_exists:
            sign = -1
            sign_exists = True
            continue

        elif (char == '+' or char == '-') and sign_exists:
            break

        # If char is a leading 0, continue (so skip it)
        if char.isdigit() and char == '0' and return_string == '':
            sign_exists = True
            continue

        # Add to string if numeric, if sign has not been yet assigned, it will be now to prevent '+1245-124' to become '-1245124'
        if char.isdigit():
            sign_exists = True
            return_string += char
    
    if return_string != '':  # If return string is not empty, return it and sign it
        return int(return_string) * sign
    else:  # Else return 0
        return 0

def main():
    atoi_sample = " -042"
    atoi_sample2 = '1337c0d3'
    atoi_sample3 = '0-1'
    atoi_sample4 = 'words and 987'
    print(myAtoi(atoi_sample))
    print(myAtoi(atoi_sample2))
    print(myAtoi(atoi_sample3))
    print(myAtoi(atoi_sample4))


main()