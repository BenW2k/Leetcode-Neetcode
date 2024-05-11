def maxArea(height):
    #int array height n, n vertical
    j = 0
    k = len(height) - 1
    area= 0
    # for i in height:
    while j <= k:
        if height[j] <= height[k]:
            if area < height[j] * (k-j):
                area = height[j] * (k-j)
            j+=1
        else:
            if area < height[k] * (k-j):
                area = height[k] * (k-j)
            k-=1
    return area