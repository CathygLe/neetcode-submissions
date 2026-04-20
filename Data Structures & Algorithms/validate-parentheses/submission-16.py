class Solution:
    def isValid(self, s: str) -> bool:
        stack = []



        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif not stack:
                return False
            else:
                popped = stack.pop()

                if popped != i:
                    return False
        return True if not stack else False