class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ''
        for i in range(len(strs[0])):
            char = strs[0][i]
           
            if all(i < len(s) and s[i] == char for s in strs):
                a += char
            else:
                break
        return a
        
        
            
            
                
                
        

        
