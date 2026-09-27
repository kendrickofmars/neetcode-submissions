class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check that string length is exactly the same
        if len(s) != len(t):
            return False

        # declaring 2 hashmaps (key is the char, val is the No. occurrences)
        # keeps track of the number occurrences of each char in each string
        countS, countT = {}, {}
        # since we know strings are of the same length, 
        # we can iterate through the values over the length of string s 
        for i in range(len(s)):
            # incrementing count when particular char is encountered in string s at index i 
            # if we tried adding 1 to just countS[s[i]], it's possible we get key doesn't exist error
            # since character may not exist in hashmap yet
            # "get" allows us to check if key exists first, and if not, default value is '0'
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # if count at character 'i' is not the same, we can immediately return false 
        for c in countS:
            # we know that they're not anagrams if count is not the same per character
            # we also use get, just in case c not in countT
            if countS[c] != countT.get(c, 0):
                return False
        # if loop exits, that means we can return True, they are anagrams 
        return True
            #print(f"s: {s} \nt: {t}")