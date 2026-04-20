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
                if stack:
                    val = stack.pop();

                    if val != b:
                        return False
                else:
                    return False
        return True

