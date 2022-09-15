def trap(height):
    tappedWater = 0
    
    x = height[0]
    indx = 0
    for ind,ele in enumerate(height):
        if ele >= x and ind>0:
            area = ((ind-indx)-1)*x
            blockedArea = sum(height[indx+1:ind])
            tappedWater += area-blockedArea
            print(ele, area, blockedArea, height[indx+1:ind], tappedWater)
            x = ele
            indx = ind
    print(tappedWater)
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
    return (tappedWater, remainingHeight)
        
height = [0,1,0,2,1,0,1,3,2,1,2,1]

ans = trap(height)
print(ans)