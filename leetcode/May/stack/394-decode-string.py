def decodeString(s: str) -> str:
    stack = []
    result = ''
    multiplier = ''

    for char in s:
        if char.isdigit():
            multiplier += char

        elif char == '[':
            stack.append([int(multiplier), ''])
            multiplier = ''

        elif char.isalpha():
            if stack:
                stack[-1][1] += char
            else:
                result += char

        elif char == ']':
            stack_top = stack.pop()
            if stack:
                stack[-1][1] += stack_top[1] * stack_top[0]
            else:
                result += stack_top[1] * stack_top[0]

    return result

def main():
    # Input: s = "2[abc]3[cd]ef"
    # Output: "abcabccdcdcdef"

    # Input: s = "3[a]2[bc]"
    # Output: "aaabcbc"

    # Input: s = "3[a2[c]ef]"
    # Output: "accaccacc"

    print(decodeString("2[abc]3[cd]ef"))
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
    print(decodeString("10[a]"))


main()