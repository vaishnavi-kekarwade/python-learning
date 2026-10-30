#Valid Palindrome (LeetCode, Easy)

#Problem in my own words:
# A palindrome reads the same forwards and backwards.
# Ignore spaces, symbols and capital letters, then check if the text is a palindrome.
# Example: "A man, a plan, a canal: Panama" -> True
#
#idea:
# 1. Make everything lowercase, so "A" and "a" count as equal.
# 2. Keep only letters and digits, and drop everything else.
# 3. Compare the cleaned text with its reverse.
#
#Time: O(n)  ---> one pass over the text
# Space: O(n) ---> a new cleaned string plus a reversed copy
#
#What I learned:-
# - isalnum() is True for letters and digits only
# - text[::-1] reverses a string
# - Next step: try the two-pointer version, which uses O(1) extra space


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Step 1: lowercase, so capitals do not matter
        s = s.lower()

        # Step 2: build a clean string with only letters and digits
        clean = ""
        for ch in s:
            if ch.isalnum():      # skip spaces,commas,colons and other symbols
                clean += ch

        # Step 3: a palindrome equals its own reverse
        return clean == clean[::-1]