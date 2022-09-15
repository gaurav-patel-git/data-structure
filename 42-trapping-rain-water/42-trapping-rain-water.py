class Solution:
    def trap(self, height: List[int]) -> int:
        tappedWater = 0
        
        x = height[0]
        indx = 0
        for ind,ele in enumerate(height):
            if ele >= x and ind>0:
                area = ((ind-indx)-1)*x
                blockedArea = sum(height[indx+1:ind])
                tappedWater += area-blockedArea
                x = ele
                indx = ind
        
        remainingHeight = height[indx:][::-1]
        x = remainingHeight[0]
        indx = 0
        for ind,ele in enumerate(remainingHeight):
            if ele >= x and ind>0:
                area = ((ind-indx)-1)*x
                blockedArea = sum(remainingHeight[indx+1:ind])
                tappedWater += area-blockedArea
                x = ele
                indx = ind
        return tappedWater
        