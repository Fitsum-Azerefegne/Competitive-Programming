class Solution:
    def isValid(self, s: str) -> bool:
        bracket_hash = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        brackets = []
        for bracket in s:
            if bracket in bracket_hash.keys():
                brackets.append(bracket)
            else:
                if brackets:
                    if bracket_hash[brackets.pop()] != bracket:
                        return False
                else:
                    return False
        if len(brackets) != 0:
            return False
        return True


      