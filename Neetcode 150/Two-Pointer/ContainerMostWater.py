def maxArea(height):
    #int array height n, n vertical
    j = 0
    k = len(height) - 1
    left = 0
    right = 0
    area=0
    # for i in height:
    while j < k:
        if height[j] <= height[k]:
            lowest_side = height[j]
        else:
            lowest_side = height[k]
        if area < lowest_side * (k-j):
            area = lowest_side * (k-j)
        if height[j] > height[k]:
            k-=1
        else:
            j+=1
    return area
                