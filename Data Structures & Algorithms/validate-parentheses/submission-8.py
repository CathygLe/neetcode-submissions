class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for bracket in s:
            if bracket == "(":
                stack.append(")")
            
            elif bracket == "{":
                stack.append("}")

            elif bracket == "[":
                stack.append("]")

            else:
                if not stack:
                    return False
                
                val = stack.pop
                if val != bracket:
                    return False
            
        if stack:
            return False 
        if not stack:
            return True




























        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:  # It's a closing bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # Pop the matching opening
                else:
                    return False  # Mismatch or empty stack
            else:
                stack.append(c)  # It's an opening bracket

        return True if not stack else False  # Valid if nothing is left unclosed

        