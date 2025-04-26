# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def longestCommonPrefix(strs: list[str]) -> str:
    if strs == [""]:
        return ''
    if len(strs) == 1:
        return strs[0]
    dictionary = {}
    dict_list = []

    for word in strs:
        counter = len(word)
        for j in range(len(word) + 1):
            dictionary[j] = word[:j]
            counter -= 1
        dict_list.append(dictionary)
        dictionary = {}

    if len(dict_list) < 1:
        common_items = (dict_list[0].items() & dict_list[1].items())
        return max(common_items)[1]

    else:
        for i in range(2, len(dict_list)):
            common_items = (dict_list[i - 2].items() & dict_list[i - 1].items() & dict_list[i].items())
        return max(common_items)[1]

            


def main():
    print(longestCommonPrefix(["flower","flow","flight"]))


main()
