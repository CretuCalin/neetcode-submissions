class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for string in strs:
            encoded_str += str(len(string)) + "?" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i=0
        while(i<len(s)):
            count_str= ""

            while s[i] != "?":
                count_str += s[i]
                i += 1

            i += 1
            count_int = int(count_str)

            current_string = ""
            while count_int > 0:
                current_string += s[i]
                count_int -= 1
                i += 1

            decoded_strings.append(current_string)

        return decoded_strings

s = Solution()
print(s.encode(["Hello","World"]))

# print("encode", s.encode([]))
# print(s.decode(s.encode([])))