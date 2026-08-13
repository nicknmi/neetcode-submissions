class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = 0    

        product = 1

        for num in nums:
            if num == 0:
                numZeros += 1
                continue

            product *= num
        

        ans = []
        for num in nums:
            if numZeros == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            elif numZeros >= 2:
                ans.append(0)
            
            else:
                ans.append(product // num)

        
        return ans
            