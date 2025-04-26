def isValid(self, s: str) -> bool:
    stack = [] # Stores open brackets
    open_parenthesis = set(['(', '[', '{']) # For checking
    combinations = set(['()', '[]', '{}']) # For checking when encounter closed bracket
    for char in s:
        if char in open_parenthesis:  # If open bracket, add to stack
            stack.append(char) 
        elif not stack:  # If closed bracket with no opening brackets
            return False
        elif stack[-1] + char not in combinations:  # If the last open bracket and closed bracket are different 
            return False
        else:  # If open and closed brackets are the same
            stack.pop()
    return not stack  # If empty - True, else - False since open brackets were left in the stack
        


            
        