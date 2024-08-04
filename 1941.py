class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        final_result = {}
        for i in s:
            if i not in final_result:
                final_result[i] = 1
            else:
                final_result[i]+=1
        print(final_result)
        return True if len(set{final_result.values}) == 1 else False
        
        

s = Solution()

s.areOccurrencesEqual('aaabb')