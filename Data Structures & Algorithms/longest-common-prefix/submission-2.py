class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 1. Pehle word ko sample bana lo
        first_word = strs[0]

        # 2. Sample ke har letter ki position par jao (0, 1, 2...)
        for i in range(len(first_word)):
            # 3. Wo letter pakdo jo sab mein dhoondhna hai
            letter = first_word[i]

            # 4. Baaki saare words mein check karo
            for word in strs:
                # 5. Word khatam ya letter alag? Toh yahin tak ka hissa return karo
                if i == len(word) or word[i] != letter:
                    return first_word[:i]

        # 6. Agar sab match ho gaya, toh poora pehla word hi answer hai
        return first_word