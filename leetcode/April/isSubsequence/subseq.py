def isSubsequence(s: str, t: str) -> bool:
    if s == '':
        return True

    slower_ptr = 0
    list_s, list_t = list(s), list(t)
    list_compare = []

    for faster_ptr in range(len(t)):
        if list_t[faster_ptr] == list_s[slower_ptr]:
            list_compare.append(list_t[faster_ptr])
            if slower_ptr < len(s) - 1:
                slower_ptr += 1
            else:
                break
    print(list_compare)
    return True if list_s == list_compare else False


def main():
    s = "xyz"
    t = "abcdefghijklmnopqrst" 
    print(isSubsequence(s, t))

main()