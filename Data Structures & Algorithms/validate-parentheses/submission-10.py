class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for b in s:
            if b =="(":
                stack.append(")")
            elif b =="{":
                stack.append("}")
            elif b =="[":
                stack.append("]")
            else:
                val = stack.pop();

                if val != b:
                    return False
        return True

