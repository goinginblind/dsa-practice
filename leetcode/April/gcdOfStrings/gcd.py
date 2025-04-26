def gcdOfStrings(str1: str, str2: str) -> str:
    def findDifference(str1, str2):
        '''Find minimal difference possible between two strings'''
        if str1 == '' or str2 == '':
            return str1 if str1 != '' else str2
        if len(str1) > len(str2):
            return findDifference(str1[len(str2):], str2)
        elif len(str2) > len(str1):
            return findDifference(str1, str2[len(str1):])
        # If lengths same, check if strings equal
        elif str1 != str2:
            return ''
        else:
            return str1

    difference = findDifference(str1, str2)

    # Since if diff exists, only this diff multiplied by some amount can be 
    # in str1 and str2, else they don't have a GCD
    if difference != '' and str1 == difference * (len(str1) // len(difference)) and str2 == difference * (len(str2) // len(difference)):
        return difference
    else:
        return ''


def main():
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    print(gcdOfStrings(str1, str2)) # 'AB'

main()