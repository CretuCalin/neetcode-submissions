class Solution:

    def _are_anagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        count_str1 = {}
        count_str2 = {}

        for i in range(len(str1)):
            if str1[i] not in count_str1:
                count_str1[str1[i]] = 0
            else:
                count_str1[str1[i]] += 1

            if str2[i] not in count_str2:
                count_str2[str2[i]] = 0
            else:
                count_str2[str2[i]] += 1

        if len(count_str1.keys()) != len(count_str2.keys()):
            return False
        
        for str1_key in count_str1.keys():
            if str1_key not in count_str2.keys():
                return False
            if count_str1[str1_key] != count_str2[str1_key]:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_anagram = []
        list_of_anagram.append([strs[0]])
        if len(strs) <= 1:
            return list_of_anagram

        for string in strs[1:]:
            matched = 0
            for sublist in list_of_anagram:
                if self._are_anagram(string, sublist[0]):
                    sublist.append(string)
                    matched = 1
                    break
            if matched == 0:
                list_of_anagram.append([string])
        return list_of_anagram


# sol = Solution()
# print(sol._are_anagram("bat", "tab"))
# # print(sol._are_anagram("", "cat"))
# # print(sol._are_anagram("asd", "qwer"))
# # print(sol._are_anagram("qwer", "rewq"))


        