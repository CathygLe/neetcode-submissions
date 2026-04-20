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
            elif not stack:
                return False

            else:
                val = stack.pop();

                if val != b:
                    return False
                
        return True if not stack else False

