class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validSet = {"()","[]", "{}"}
        for char in s:
            if(char == '(' or char == '{' or char == '['):
                stack.insert(0, char)
            if((char == ')' or char == '}' or char == ']')):
                if(len(stack) == 0):
                    return False
                removed = stack.pop(0)
                if(removed + char not in validSet):
                    return False
        return True if len(stack) == 0 else False
            

