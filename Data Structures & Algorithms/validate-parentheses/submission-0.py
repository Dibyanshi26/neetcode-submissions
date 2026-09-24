class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # Agar character closing bracket hai
            if char in close_to_open:
                # Stack non-empty ho aur top element match kare
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket mila, stack me push karo
                stack.append(char)

        # Aakhri me stack empty hona chahiye (saare open brackets close ho chuke hon)
        return len(stack) == 0