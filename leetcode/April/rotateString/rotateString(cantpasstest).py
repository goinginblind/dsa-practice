def rotateString(s: str, goal: str) -> bool:
    goalList = list(goal)
    sList = list(s)
    if len(s) != len(goal):
        return False
    diff = ord(s[0]) - ord(goal[0])
    if diff == 0:
        for i in range(len(s)):
            if s[i] != goal[i]:
                return False
        return True
    elif diff > 0:
        for i in range(diff):
            char = goalList.pop(0)  
            goalList.append(char)
        if ''.join(goalList) != s:
            return False
    elif diff < 0:
        for i in range((diff) * -1):
            char = goalList.pop(-1)  
            goalList.insert(0, char)
        if ''.join(goalList) != s:
            return False
    return True

           


def main():
    print(rotateString(s = "defdefdefabcabc", goal = "defdefabcabcdef"))


main()