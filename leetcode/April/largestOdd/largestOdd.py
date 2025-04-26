def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]


        
def main():
    print(largestOddNumber("357373"))

main()