def isPalindrome(x: int) -> bool:
    asString = f'{x}'

    for i in range(len(asString) // 2):
        if asString[i] != asString[-i-1]:
            return False
        
    return True

def main():
    print(isPalindrome())

main()