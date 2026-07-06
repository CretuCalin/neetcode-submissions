class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                clean_s += char.lower()

        print(clean_s)

        # if len(clean_s) % 2 == 1:
        #     return False

        for i in range(int(len(clean_s) / 2)):
            j = len(clean_s) - i - 1
            if clean_s[i] != clean_s[j]:
                print(clean_s[i], clean_s[j])
                return False
        return True

        


sol = Solution()
sol.isPalindrome("Was it a car or a cat I saw?")