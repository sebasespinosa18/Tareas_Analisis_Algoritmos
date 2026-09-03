class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0  # Puntero para niños
        j = 0  # Puntero para galletas
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
            
        return i