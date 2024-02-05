class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = []
        count = []
        for i in range(len(s)):
            if s[i] in visited:
                try:
                    count.remove(s.index(s[i]))
                except ValueError:
                    continue
            else: 
                visited.append(s[i])
                count.append(i)
        return -1 if len(count) == 0 else count[0]
