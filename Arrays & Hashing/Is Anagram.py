class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    sol = Solution()
    s = "racecar"
    t = "carrace"
    print(sol.isAnagram(s, t))

    s = "jar"
    t = "jam"
    print(sol.isAnagram(s, t))
