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
            else:
                popped = stack.pop()

                if popped != i:
                    return False
        return True