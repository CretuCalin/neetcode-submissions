class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            if s[i] not in count_s:
                count_s[s[i]] = 0
            else:
                count_s[s[i]] += 1

            if t[i] not in count_t:
                count_t[t[i]] = 0
            else:
                count_t[t[i]] += 1

        if len(count_s) != len(count_t):
            return False

        for count_s_key in count_s.keys():
            if count_s_key not in count_t.keys():
                return False

            if count_s[count_s_key] != count_t[count_s_key]:
                return False        
        return True
        