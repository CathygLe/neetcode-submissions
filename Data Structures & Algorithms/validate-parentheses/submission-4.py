class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)%2:
        #     return False 

        stack = []

        for bracket in s:
            if bracket == "[":
                stack.append("]")

            elif bracket == "(":
                stack.append(")")

            elif bracket == "{":
                stack.append("}")
            else: 
                if not stack:
                    return False 

                openBracket = stack.pop()

                if openBracket != bracket:
                    return False

        return False if stack else True  

            



        





























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

        