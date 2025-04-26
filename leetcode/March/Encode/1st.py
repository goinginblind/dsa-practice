# Input: ["neet","code","love","you"]
# 
# Output:["neet","code","love","you"]



def encode(strs: list[str]) -> str:
    string = ''
    for i in strs:
        string = string + i + '\$%'
    return string

def decode(s: str) -> list[str]:
    return_string = s.split('\$%')
    del return_string[len(return_string) - 1]
    return return_string 

def main():
    print(encode(["neet","code","love","you"]))
    print(decode(encode(["neet","code","love","you"])))

main()