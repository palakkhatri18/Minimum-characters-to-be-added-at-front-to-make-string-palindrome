# Given string str of length N. The task is to find the minimum characters to be added at the front to make string palindrome.
# Note: A palindrome is a word which reads the same backward as forward. Example: "madam".

class Solution:
    def minChar(self, str):
        def computeLPSArray(s):
            n = len(s)
            lps = [0] * n
            length = 0
            i = 1
            while i < n:
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Create the concatenated string
        rev_str = str[::-1]
        concat_str = str + '#' + rev_str
        
        # Get the LPS array for the concatenated string
        lps = computeLPSArray(concat_str)
        
        # The number of characters to be added is the difference between the 
        # length of the original string and the length of the longest prefix 
        # which is also a suffix.
        return len(str) - lps[-1]  