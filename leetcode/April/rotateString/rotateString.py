def rotateString(s: str, goal: str) -> bool:
    # If strings are the same, no rotation was made
    if s == goal:
        return True
    
    # Setup two pointers, compare sliced goal to the s
    for i in range(-1, -len(goal), -1):
        if goal[i] == s[0] and s == goal[i:-1] + goal[-1] + goal[0:i]:
            return True
        
    return False
    

def main():
    print(rotateString(s = "gcmbf", goal = "fgcmb"))

main()

