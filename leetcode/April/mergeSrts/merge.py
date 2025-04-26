def mergeAlternately(word1: str, word2: str) -> str:
    merged_string = []
    i = j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged_string.append(word1[i])
            i += 1
        if j < len(word2):
            merged_string.append(word2[j])
            j += 1
    
    return ''.join(merged_string)











def main():
    word1 = "123"
    word2 = "4"
    print(mergeAlternately(word1, word2))


main()