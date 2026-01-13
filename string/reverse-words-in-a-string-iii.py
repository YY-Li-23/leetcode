class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split(" ")-> ["Let's","take","LeetCode","contest"] -> list[str]
        return " ".join(i[::-1] for i in s.split(" ")) #"abc"[::-1]      # "cba"

        #words = ["Mr", "Ding"] & " ".join(words)->"Mr Ding"

                
        