class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'bubibaca'
        return "\n".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "bubibaca":
            return []
        return s.split("\n")

# s = Solution()

# print("encode", s.encode([]))
# print(s.decode(s.encode([])))